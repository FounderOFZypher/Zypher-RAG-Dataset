"""Additional advanced retrieval utilities — query expansion, parent docs, freshness."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Iterable

from brain.types import Document, ScoredDocument

_TOKEN_RE = re.compile(r"[a-z0-9_]+", re.IGNORECASE)

# Lightweight synonym / expansion map for RAG engineering queries
_EXPANSIONS: dict[str, tuple[str, ...]] = {
    "rag": ("retrieval augmented generation", "hybrid retrieval", "vector search"),
    "graphrag": ("knowledge graph retrieval", "graph expansion", "multi-hop"),
    "bm25": ("sparse retrieval", "lexical search", "okapi"),
    "embedding": ("vector", "dense retrieval", "sentence transformer"),
    "api": ("endpoint", "rest", "openapi", "http"),
    "sql": ("query", "schema", "postgres", "select"),
    "auth": ("authentication", "authorization", "jwt", "oauth"),
    "k8s": ("kubernetes", "pod", "deployment", "helm"),
    "incident": ("outage", "postmortem", "runbook", "oncall"),
}


def expand_query(query: str, max_extra_terms: int = 8) -> str:
    """Deterministic query expansion for recall without an LLM."""
    tokens = _TOKEN_RE.findall(query.lower())
    extras: list[str] = []
    for tok in tokens:
        for phrase in _EXPANSIONS.get(tok, ()):
            extras.append(phrase)
            if len(extras) >= max_extra_terms:
                break
        if len(extras) >= max_extra_terms:
            break
    if not extras:
        return query
    return f"{query} {' '.join(extras)}"


def freshness_boost(
    documents: list[ScoredDocument],
    half_life_days: float = 180.0,
) -> list[ScoredDocument]:
    """
    Soft boost for newer documents when a date-like token appears in the path/title.
    Falls back to neutral when no date is found.
    """
    now = datetime.now(timezone.utc)
    year_re = re.compile(r"(20\d{2})")
    out: list[ScoredDocument] = []
    for scored in documents:
        blob = f"{scored.document.path} {scored.document.title}"
        years = [int(y) for y in year_re.findall(blob)]
        boost = 1.0
        if years:
            age_years = max(0, now.year - max(years))
            age_days = age_years * 365
            boost = 0.85 + 0.15 * (0.5 ** (age_days / max(half_life_days, 1)))
        out.append(ScoredDocument(
            document=scored.document,
            score=scored.score * boost,
            source=f"{scored.source}+freshness" if boost != 1.0 else scored.source,
        ))
    out.sort(key=lambda s: s.score, reverse=True)
    return out


def parent_document_expand(
    documents: list[ScoredDocument],
    kb_documents: Iterable[Document],
    max_parents: int = 3,
) -> list[ScoredDocument]:
    """
    Parent-document retrieval: if a hit looks like a section/chunk path,
    also surface the parent hub / related canonical doc.
    """
    by_id = {d.doc_id: d for d in kb_documents}
    by_hub: dict[str, list[Document]] = {}
    for d in kb_documents:
        if d.hub:
            by_hub.setdefault(d.hub, []).append(d)

    extras: list[ScoredDocument] = []
    seen = {s.document.doc_id for s in documents}
    for scored in documents[: max_parents * 2]:
        doc = scored.document
        # related parents
        for rel in (doc.related or [])[:2]:
            parent = by_id.get(rel)
            if parent and parent.doc_id not in seen:
                seen.add(parent.doc_id)
                extras.append(ScoredDocument(
                    document=parent,
                    score=scored.score * 0.72,
                    source=f"{scored.source}+parent",
                ))
        # hub canonical
        if doc.hub and doc.hub in by_hub:
            for cand in by_hub[doc.hub]:
                if cand.doc_id not in seen and cand.doc_type in {"documentation", "guide", "api_reference"}:
                    seen.add(cand.doc_id)
                    extras.append(ScoredDocument(
                        document=cand,
                        score=scored.score * 0.65,
                        source=f"{scored.source}+hub_parent",
                    ))
                    break
        if len(extras) >= max_parents:
            break
    return list(documents) + extras
