"""BM25 sparse lexical retrieval for hybrid RAG."""

from __future__ import annotations

import math
import re
from collections import Counter, defaultdict

from brain.ingestion.loader import KnowledgeBase
from brain.types import Document, ScoredDocument

_TOKEN_RE = re.compile(r"[a-z0-9_]+", re.IGNORECASE)


def tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower())


class BM25Index:
    """Okapi BM25 over the knowledge base (pure Python, no extra deps)."""

    def __init__(self, kb: KnowledgeBase, k1: float = 1.5, b: float = 0.75):
        self.kb = kb
        self.k1 = k1
        self.b = b
        self._docs: list[Document] = []
        self._doc_lens: list[int] = []
        self._tf: list[Counter[str]] = []
        self._df: dict[str, int] = defaultdict(int)
        self._avgdl = 0.0
        self._by_id: dict[str, Document] = {}
        self.build()

    def build(self) -> None:
        self._docs = list(self.kb.documents)
        self._by_id = {d.doc_id: d for d in self._docs}
        self._tf = []
        self._doc_lens = []
        self._df = defaultdict(int)
        for doc in self._docs:
            tokens = tokenize(f"{doc.title} {doc.doc_type} {doc.category} {' '.join(doc.tags)} {doc.content[:6000]}")
            counts = Counter(tokens)
            self._tf.append(counts)
            self._doc_lens.append(len(tokens) or 1)
            for term in counts:
                self._df[term] += 1
        n = len(self._docs) or 1
        self._avgdl = sum(self._doc_lens) / n
        self._n = n

    def refresh(self) -> None:
        self.build()

    def upsert(self, doc: Document) -> None:
        """Rebuild is acceptable for moderate corpora; call refresh after batch adds."""
        self.refresh()

    def delete(self, doc_id: str) -> None:
        self.refresh()

    def search(self, query: str, top_k: int = 15) -> list[ScoredDocument]:
        q_tokens = tokenize(query)
        if not q_tokens or not self._docs:
            return []
        scores: list[tuple[float, Document]] = []
        for i, doc in enumerate(self._docs):
            score = self._score_doc(q_tokens, i)
            if score > 0:
                scores.append((score, doc))
        scores.sort(key=lambda x: x[0], reverse=True)
        if not scores:
            return []
        max_score = scores[0][0] or 1.0
        return [
            ScoredDocument(document=doc, score=round(raw / max_score, 6), source="bm25")
            for raw, doc in scores[:top_k]
        ]

    def _score_doc(self, q_tokens: list[str], idx: int) -> float:
        score = 0.0
        dl = self._doc_lens[idx]
        tf = self._tf[idx]
        for term in q_tokens:
            df = self._df.get(term, 0)
            if df == 0:
                continue
            idf = math.log(1 + (self._n - df + 0.5) / (df + 0.5))
            freq = tf.get(term, 0)
            denom = freq + self.k1 * (1 - self.b + self.b * dl / self._avgdl)
            score += idf * (freq * (self.k1 + 1)) / (denom or 1.0)
        return score
