"""Retrieval explainability — why did Coltex retrieve this?"""

from __future__ import annotations

import re
import time
from typing import Any


class ExplainEngine:
    """Explainable retrieval across all advanced RAG sources."""

    def __init__(self, brain, monitor=None):
        self._brain = brain
        self._monitor = monitor

    def explain(self, query: str, top_k: int = 5, mode: str | None = None) -> dict[str, Any]:
        start = time.perf_counter()
        result = self._brain.retrieve(query, mode=mode or "hybrid", top_k=top_k)
        pipeline = self._brain.retrieval
        trace = getattr(result, "trace", None) or {}

        # Re-run individual stages for factor attribution when available
        stage_ids: dict[str, set[str]] = {}
        try:
            stage_ids["vector"] = {s.document.doc_id for s in pipeline.vector_index.search(query, top_k=top_k * 2)}
        except Exception:
            stage_ids["vector"] = set()
        try:
            stage_ids["metadata"] = {s.document.doc_id for s in pipeline.metadata_index.search(query, top_k=top_k * 2)}
        except Exception:
            stage_ids["metadata"] = set()
        if getattr(pipeline, "bm25_index", None) is not None:
            try:
                stage_ids["bm25"] = {s.document.doc_id for s in pipeline.bm25_index.search(query, top_k=top_k * 2)}
            except Exception:
                stage_ids["bm25"] = set()
        for name, retriever in (
            ("sql", getattr(pipeline, "sql_retriever", None)),
            ("code", getattr(pipeline, "code_retriever", None)),
            ("api", getattr(pipeline, "api_retriever", None)),
        ):
            if retriever is not None:
                try:
                    stage_ids[name] = {s.document.doc_id for s in retriever.search(query, top_k=top_k * 2)}
                except Exception:
                    stage_ids[name] = set()
        if getattr(pipeline, "multi_vector_index", None) is not None and pipeline.multi_vector_index.is_indexed:
            try:
                stage_ids["multi_vector"] = {
                    s.document.doc_id for s in pipeline.multi_vector_index.search(query, top_k=top_k * 2)
                }
            except Exception:
                stage_ids["multi_vector"] = set()

        query_lower = query.lower()
        query_tokens = set(re.findall(r"\w+", query_lower))

        explanations = []
        for scored in result.documents:
            doc = scored.document
            reasons: list[dict[str, Any]] = []
            source_parts = set(str(scored.source).split("+"))

            for stage, label in (
                ("vector", "Vector Similarity"),
                ("bm25", "BM25 Lexical Match"),
                ("metadata", "Metadata Match"),
                ("graph", "GraphRAG Expansion"),
                ("multi_vector", "Multi-Vector Match"),
                ("sql", "SQL Retrieval"),
                ("code", "Code Retrieval"),
                ("api", "API Retrieval"),
                ("cross_encoder", "Cross-Encoder Rerank"),
                ("lexical_rerank", "Lexical Rerank"),
                ("plugin", "Plugin Search"),
            ):
                if stage in source_parts or doc.doc_id in stage_ids.get(stage, set()):
                    reasons.append({
                        "factor": stage,
                        "label": label,
                        "detail": f"Matched via {stage} retrieval",
                    })

            if doc.doc_type:
                reasons.append({
                    "factor": "doc_type",
                    "label": "Document Type",
                    "detail": doc.doc_type,
                })
            title_lower = (doc.title or "").lower()
            if any(t in title_lower for t in query_tokens if len(t) > 2):
                reasons.append({"factor": "title_match", "label": "Title Match", "detail": doc.title})

            if doc.hub:
                reasons.append({"factor": "hub", "label": "Knowledge Hub", "detail": doc.hub})

            explanations.append({
                "document_id": doc.doc_id,
                "title": doc.title,
                "final_score": round(scored.score, 4),
                "retrieval_sources": scored.source,
                "why": reasons,
                "summary": self._summarize(reasons),
            })

        elapsed_ms = round((time.perf_counter() - start) * 1000, 1)
        if self._monitor:
            self._monitor.record_search_latency(elapsed_ms / 1000)

        return {
            "engine": "explain",
            "query": query,
            "mode": mode or "hybrid",
            "latency_ms": elapsed_ms,
            "trace": trace,
            "capabilities": self._brain.capabilities() if hasattr(self._brain, "capabilities") else {},
            "results": explanations,
        }

    @staticmethod
    def _summarize(reasons: list[dict[str, Any]]) -> str:
        labels = [r["label"] for r in reasons[:5]]
        return " · ".join(labels)
