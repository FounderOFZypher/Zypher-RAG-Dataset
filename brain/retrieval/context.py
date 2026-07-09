"""Context builder and compression for RAG answer assembly."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from brain.types import ScoredDocument

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
_WS = re.compile(r"\s+")


@dataclass
class ContextBlock:
    rank: int
    doc_id: str
    title: str
    path: str
    source: str
    score: float
    doc_type: str
    category: str
    hub: str
    text: str
    compressed: bool = False
    chars: int = 0

    def to_markdown(self) -> str:
        meta = f"doc_type={self.doc_type or 'unknown'}, category={self.category or 'unknown'}"
        if self.hub:
            meta += f", hub={self.hub}"
        flag = " compressed" if self.compressed else ""
        return (
            f"### [{self.rank}] {self.title}\n"
            f"Source: {self.path}\n"
            f"Metadata: {meta}\n"
            f"Relevance: {self.score:.2f} ({self.source}){flag}\n\n"
            f"{self.text}"
        )


@dataclass
class BuiltContext:
    query: str
    blocks: list[ContextBlock] = field(default_factory=list)
    text: str = ""
    total_chars: int = 0
    compressed_blocks: int = 0
    modes_used: list[str] = field(default_factory=list)
    explain: dict[str, Any] = field(default_factory=dict)

    def as_string(self) -> str:
        return self.text


class ContextCompressor:
    """
    Extractive context compression.

    Keeps query-relevant sentences and drops low-signal padding so more
    documents fit in the context window without an LLM dependency.
    """

    def __init__(self, keep_ratio: float = 0.45, min_chars: int = 280, max_chars: int = 1800):
        self.keep_ratio = keep_ratio
        self.min_chars = min_chars
        self.max_chars = max_chars

    def compress(self, query: str, text: str) -> tuple[str, bool]:
        if len(text) <= self.min_chars:
            return text, False
        q_tokens = set(re.findall(r"[a-z0-9_]+", query.lower()))
        sentences = [s.strip() for s in _SENTENCE_SPLIT.split(text) if s.strip()]
        if len(sentences) <= 2:
            clipped = text[: self.max_chars]
            return clipped, clipped != text

        scored: list[tuple[float, str]] = []
        for i, sent in enumerate(sentences):
            tokens = set(re.findall(r"[a-z0-9_]+", sent.lower()))
            overlap = len(q_tokens & tokens) / max(len(q_tokens), 1)
            # prefer early sentences slightly (lead bias)
            position = 1.0 - (i / max(len(sentences), 1)) * 0.25
            scored.append((overlap * 0.8 + position * 0.2, sent))

        scored.sort(key=lambda x: x[0], reverse=True)
        keep_n = max(2, int(len(sentences) * self.keep_ratio))
        chosen = {s for _, s in scored[:keep_n]}
        # preserve original order
        ordered = [s for s in sentences if s in chosen]
        compressed = " ".join(ordered)
        compressed = _WS.sub(" ", compressed).strip()
        if len(compressed) > self.max_chars:
            compressed = compressed[: self.max_chars].rsplit(" ", 1)[0] + "…"
        changed = compressed != text and len(compressed) < len(text)
        return compressed or text[: self.max_chars], changed


class ContextBuilder:
    """
    Assembles a structured, optionally compressed context window for RAG.

    Features:
      - ranked blocks with metadata headers
      - extractive compression
      - diversity by doc_type / category
      - source attribution for explainable retrieval
    """

    def __init__(
        self,
        max_chars: int = 20000,
        per_doc_chars: int = 2500,
        compress: bool = True,
        diversity: bool = True,
        compressor: ContextCompressor | None = None,
    ):
        self.max_chars = max_chars
        self.per_doc_chars = per_doc_chars
        self.compress = compress
        self.diversity = diversity
        self.compressor = compressor or ContextCompressor(max_chars=per_doc_chars)

    def build(self, query: str, documents: list[ScoredDocument]) -> BuiltContext:
        if not documents:
            return BuiltContext(
                query=query,
                text="No relevant documents found in Coltex.",
                explain={"empty": True},
            )

        selected = self._select(documents)
        blocks: list[ContextBlock] = []
        used = 0
        compressed_count = 0
        modes: set[str] = set()

        for i, scored in enumerate(selected, start=1):
            doc = scored.document
            raw = doc.content[: self.per_doc_chars * 2]
            text, was_compressed = (raw, False)
            if self.compress:
                text, was_compressed = self.compressor.compress(query, raw)
                text = text[: self.per_doc_chars]
            else:
                text = raw[: self.per_doc_chars]
            if was_compressed:
                compressed_count += 1
            for part in str(scored.source).split("+"):
                modes.add(part)
            block = ContextBlock(
                rank=i,
                doc_id=doc.doc_id,
                title=doc.title,
                path=doc.path,
                source=scored.source,
                score=scored.score,
                doc_type=doc.doc_type,
                category=doc.category,
                hub=doc.hub,
                text=text,
                compressed=was_compressed,
                chars=len(text),
            )
            md = block.to_markdown()
            if used + len(md) > self.max_chars:
                break
            blocks.append(block)
            used += len(md)

        text = "\n\n---\n\n".join(b.to_markdown() for b in blocks)
        return BuiltContext(
            query=query,
            blocks=blocks,
            text=text,
            total_chars=len(text),
            compressed_blocks=compressed_count,
            modes_used=sorted(modes),
            explain={
                "documents": len(blocks),
                "compressed_blocks": compressed_count,
                "modes_used": sorted(modes),
                "max_chars": self.max_chars,
            },
        )

    def _select(self, documents: list[ScoredDocument]) -> list[ScoredDocument]:
        if not self.diversity:
            return documents
        seen_types: dict[str, int] = {}
        primary: list[ScoredDocument] = []
        overflow: list[ScoredDocument] = []
        for scored in documents:
            dt = scored.document.doc_type or "unknown"
            if seen_types.get(dt, 0) < 3:
                primary.append(scored)
                seen_types[dt] = seen_types.get(dt, 0) + 1
            else:
                overflow.append(scored)
        return primary + overflow
