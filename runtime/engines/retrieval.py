"""Retrieval engine — advanced hybrid retrieval wrapper."""

from __future__ import annotations

from typing import Any


class RetrievalEngine:
    def __init__(self, brain):
        self._brain = brain

    def retrieve(
        self,
        query: str,
        *,
        with_context: bool = False,
        mode: str | None = None,
        filters: dict[str, Any] | None = None,
        top_k: int | None = None,
    ) -> dict[str, Any]:
        result = self._brain.retrieve(query, mode=mode, filters=filters, top_k=top_k)
        out: dict[str, Any] = {
            "query": query,
            "mode": mode or getattr(self._brain.retrieval, "default_mode", "hybrid"),
            "documents": [
                {
                    "id": s.document.doc_id,
                    "title": s.document.title,
                    "score": s.score,
                    "source": s.source,
                    "doc_type": s.document.doc_type,
                }
                for s in result.documents
            ],
            "trace": getattr(result, "trace", None),
        }
        if with_context:
            out["context"] = result.context
        return out

    def stats(self) -> dict[str, Any]:
        caps = self._brain.capabilities() if hasattr(self._brain, "capabilities") else {}
        return {"engine": "retrieval", "status": "active", "capabilities": caps}
