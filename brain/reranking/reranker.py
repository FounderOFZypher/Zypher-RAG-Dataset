"""Merge and re-rank retrieval results from multiple sources."""

from __future__ import annotations

from brain.types import ScoredDocument

SOURCE_WEIGHTS = {
    "vector": 1.0,
    "bm25": 0.95,
    "metadata": 0.88,
    "graph": 0.75,
    "multi_vector": 1.05,
    "sql": 0.92,
    "code": 0.92,
    "api": 0.92,
    "plugin": 0.9,
}


class Reranker:
    """Weighted multi-source fusion (pre–cross-encoder stage)."""

    def __init__(self, source_weights: dict[str, float] | None = None):
        self.weights = {**SOURCE_WEIGHTS, **(source_weights or {})}

    def merge(self, *result_sets: list[ScoredDocument], top_k: int = 10) -> list[ScoredDocument]:
        combined: dict[str, ScoredDocument] = {}
        for results in result_sets:
            for item in results:
                doc_id = item.document.doc_id
                # use primary source token for weighting
                primary = str(item.source).split("+")[0]
                weighted = item.score * self.weights.get(primary, self.weights.get(item.source, 0.5))
                if doc_id in combined:
                    existing = combined[doc_id]
                    combined[doc_id] = ScoredDocument(
                        document=existing.document,
                        score=existing.score + weighted,
                        source=f"{existing.source}+{item.source}",
                    )
                else:
                    combined[doc_id] = ScoredDocument(
                        document=item.document,
                        score=weighted,
                        source=item.source,
                    )
        ranked = sorted(combined.values(), key=lambda s: s.score, reverse=True)
        return ranked[:top_k]

    def reciprocal_rank_fusion(
        self,
        *result_sets: list[ScoredDocument],
        top_k: int = 10,
        k: int = 60,
    ) -> list[ScoredDocument]:
        """Optional RRF fusion for hybrid retrieval research comparisons."""
        scores: dict[str, float] = {}
        docs: dict[str, ScoredDocument] = {}
        for results in result_sets:
            for rank, item in enumerate(results, start=1):
                doc_id = item.document.doc_id
                scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
                if doc_id not in docs or item.score > docs[doc_id].score:
                    docs[doc_id] = item
        ranked_ids = sorted(scores.keys(), key=lambda d: scores[d], reverse=True)[:top_k]
        out: list[ScoredDocument] = []
        for doc_id in ranked_ids:
            base = docs[doc_id]
            out.append(ScoredDocument(
                document=base.document,
                score=round(scores[doc_id], 6),
                source=f"{base.source}+rrf",
            ))
        return out
