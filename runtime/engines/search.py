"""Search engine — advanced hybrid retrieval over knowledge objects."""

from __future__ import annotations

from typing import Any


class SearchEngine:
    """
    Universal search with retrieval modes:

      hybrid | vector | graphrag | bm25 | metadata
      sql | code | api | multi_vector
    """

    def __init__(self, brain):
        self._brain = brain

    def search(
        self,
        query: str,
        mode: str | None = None,
        filters: dict[str, Any] | None = None,
        top_k: int | None = None,
        explain: bool = False,
    ) -> dict[str, Any]:
        result = self._brain.retrieve(query, mode=mode, filters=filters, top_k=top_k)
        payload: dict[str, Any] = {
            "query": query,
            "mode": mode or getattr(self._brain.retrieval, "default_mode", "hybrid"),
            "results": [
                {
                    "id": s.document.doc_id,
                    "title": s.document.title,
                    "score": round(s.score, 4),
                    "source": s.source,
                    "doc_type": s.document.doc_type,
                    "category": s.document.category,
                    "hub": s.document.hub,
                    "path": s.document.path,
                }
                for s in result.documents
            ],
            "context_chars": len(result.context),
            "capabilities": self._brain.capabilities() if hasattr(self._brain, "capabilities") else {},
        }
        if explain and getattr(result, "trace", None):
            payload["trace"] = result.trace
        if explain and getattr(result, "built_context", None) is not None:
            built = result.built_context
            payload["context_meta"] = getattr(built, "explain", {})
        return payload

    def stats(self) -> dict[str, Any]:
        return {"engine": "search", "status": "active", **self._brain.stats()}
