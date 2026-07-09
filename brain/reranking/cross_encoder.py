"""Cross-encoder reranking with graceful lexical fallback."""

from __future__ import annotations

import re
from typing import Any

from brain.types import ScoredDocument

_TOKEN_RE = re.compile(r"[a-z0-9_]+", re.IGNORECASE)


class CrossEncoderReranker:
    """
    Neural cross-encoder reranker.

    Uses sentence-transformers CrossEncoder when available; otherwise falls back
    to a strong lexical overlap scorer so retrieval never hard-fails offline.
    """

    def __init__(
        self,
        model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2",
        enabled: bool = True,
        max_length: int = 512,
    ):
        self.model_name = model_name
        self.enabled = enabled
        self.max_length = max_length
        self._model = None
        self._backend = "uninitialized"

    def _ensure(self) -> None:
        if not self.enabled:
            self._backend = "disabled"
            return
        if self._backend != "uninitialized":
            return
        try:
            from sentence_transformers import CrossEncoder

            self._model = CrossEncoder(self.model_name, max_length=self.max_length)
            self._backend = "cross_encoder"
        except Exception:
            self._model = None
            self._backend = "lexical_fallback"

    @property
    def backend(self) -> str:
        self._ensure()
        return self._backend

    def rerank(
        self,
        query: str,
        documents: list[ScoredDocument],
        top_k: int | None = None,
    ) -> list[ScoredDocument]:
        if not documents:
            return []
        self._ensure()
        k = top_k or len(documents)
        if self._backend == "cross_encoder" and self._model is not None:
            return self._neural_rerank(query, documents, k)
        return self._lexical_rerank(query, documents, k)

    def _neural_rerank(
        self, query: str, documents: list[ScoredDocument], top_k: int
    ) -> list[ScoredDocument]:
        pairs = [
            [query, f"{s.document.title}\n{s.document.content[:1200]}"]
            for s in documents
        ]
        scores = self._model.predict(pairs)
        ranked = sorted(
            zip(documents, scores),
            key=lambda x: float(x[1]),
            reverse=True,
        )
        out: list[ScoredDocument] = []
        for scored, ce_score in ranked[:top_k]:
            # blend prior fusion score with cross-encoder signal
            blended = 0.35 * scored.score + 0.65 * self._sigmoid(float(ce_score))
            out.append(ScoredDocument(
                document=scored.document,
                score=round(blended, 6),
                source=f"{scored.source}+cross_encoder",
            ))
        return out

    def _lexical_rerank(
        self, query: str, documents: list[ScoredDocument], top_k: int
    ) -> list[ScoredDocument]:
        q_tokens = set(_TOKEN_RE.findall(query.lower()))
        rescored: list[ScoredDocument] = []
        for scored in documents:
            doc = scored.document
            blob = f"{doc.title} {doc.content[:2000]}".lower()
            d_tokens = set(_TOKEN_RE.findall(blob))
            overlap = len(q_tokens & d_tokens) / max(len(q_tokens), 1)
            title_hit = 0.2 if any(t in doc.title.lower() for t in q_tokens if len(t) > 2) else 0.0
            blended = 0.45 * scored.score + 0.55 * (overlap + title_hit)
            rescored.append(ScoredDocument(
                document=doc,
                score=round(blended, 6),
                source=f"{scored.source}+lexical_rerank",
            ))
        rescored.sort(key=lambda s: s.score, reverse=True)
        return rescored[:top_k]

    @staticmethod
    def _sigmoid(x: float) -> float:
        # numerically stable-ish sigmoid for CE logits
        if x >= 0:
            z = pow(2.718281828, -x)
            return 1.0 / (1.0 + z)
        z = pow(2.718281828, x)
        return z / (1.0 + z)

    def stats(self) -> dict[str, Any]:
        return {
            "enabled": self.enabled,
            "model": self.model_name,
            "backend": self.backend,
        }
