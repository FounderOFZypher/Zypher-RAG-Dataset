"""Advanced hybrid retrieval pipeline for Coltex Mega RAG."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable

from brain.graph.relationships import GraphIndex
from brain.indexing.bm25_index import BM25Index
from brain.indexing.multi_vector_index import MultiVectorIndex
from brain.indexing.vector_index import VectorIndex
from brain.metadata.index import MetadataIndex
from brain.reranking.cross_encoder import CrossEncoderReranker
from brain.reranking.reranker import Reranker
from brain.retrieval.advanced import expand_query, freshness_boost, parent_document_expand
from brain.retrieval.context import BuiltContext, ContextBuilder
from brain.retrieval.specialized import APIRetriever, CodeRetriever, SQLRetriever
from brain.types import RetrievalResult, ScoredDocument

# Keep legacy build_context import path working
from brain.retrieval.context import ContextBuilder as _CB


def build_context(documents: list[ScoredDocument], max_chars: int = 14000) -> str:
    """Backward-compatible context builder used by older call sites."""
    return ContextBuilder(max_chars=max_chars, compress=False).build("", documents).text


DEFAULT_SOURCE_WEIGHTS = {
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

MODE_ALIASES = {
    "hybrid": "hybrid",
    "vector": "vector",
    "vector_rag": "vector",
    "graphrag": "graphrag",
    "graph": "graphrag",
    "bm25": "bm25",
    "metadata": "metadata",
    "sql": "sql",
    "code": "code",
    "api": "api",
    "multi_vector": "multi_vector",
    "multivec": "multi_vector",
    "auto": "hybrid",
    "rrf": "rrf",
}


@dataclass
class RetrievalTrace:
    """Explainable retrieval trace for debugging and UI."""

    query: str
    mode: str
    stages: dict[str, int] = field(default_factory=dict)
    sources_used: list[str] = field(default_factory=list)
    reranker: str = ""
    compression: dict[str, Any] = field(default_factory=dict)
    plugin_hits: int = 0

    def as_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "mode": self.mode,
            "stages": self.stages,
            "sources_used": self.sources_used,
            "reranker": self.reranker,
            "compression": self.compression,
            "plugin_hits": self.plugin_hits,
        }


class RetrievalPipeline:
    """
    Coltex advanced retrieval flow:

      Vector RAG · BM25 · Metadata · GraphRAG · Multi-Vector
      SQL · Code · API · Hybrid fusion · Cross-Encoder rerank
      Context compression · Context builder · Explainable trace
      Plugin search algorithms
    """

    def __init__(
        self,
        vector_index: VectorIndex,
        metadata_index: MetadataIndex,
        graph_index: GraphIndex,
        bm25_index: BM25Index | None = None,
        multi_vector_index: MultiVectorIndex | None = None,
        sql_retriever: SQLRetriever | None = None,
        code_retriever: CodeRetriever | None = None,
        api_retriever: APIRetriever | None = None,
        reranker: Reranker | None = None,
        cross_encoder: CrossEncoderReranker | None = None,
        context_builder: ContextBuilder | None = None,
        plugin_manager=None,
        vector_top_k: int = 10,
        metadata_top_k: int = 8,
        bm25_top_k: int = 15,
        specialized_top_k: int = 10,
        final_top_k: int = 8,
        max_context_chars: int = 14000,
        enable_bm25: bool = True,
        enable_multi_vector: bool = True,
        enable_specialized: bool = True,
        enable_cross_encoder: bool = True,
        enable_compression: bool = True,
        default_mode: str = "hybrid",
        source_weights: dict[str, float] | None = None,
        enable_query_expansion: bool = True,
        enable_parent_documents: bool = True,
        enable_freshness: bool = True,
        fusion: str = "weighted",  # weighted | rrf
    ):
        self.vector_index = vector_index
        self.metadata_index = metadata_index
        self.graph_index = graph_index
        self.bm25_index = bm25_index
        self.multi_vector_index = multi_vector_index
        self.sql_retriever = sql_retriever
        self.code_retriever = code_retriever
        self.api_retriever = api_retriever
        weights = {**DEFAULT_SOURCE_WEIGHTS, **(source_weights or {})}
        self.reranker = reranker or Reranker(weights)
        self.cross_encoder = cross_encoder or CrossEncoderReranker(enabled=enable_cross_encoder)
        self.context_builder = context_builder or ContextBuilder(
            max_chars=max_context_chars,
            compress=enable_compression,
        )
        self.plugin_manager = plugin_manager
        self.vector_top_k = vector_top_k
        self.metadata_top_k = metadata_top_k
        self.bm25_top_k = bm25_top_k
        self.specialized_top_k = specialized_top_k
        self.final_top_k = final_top_k
        self.max_context_chars = max_context_chars
        self.enable_bm25 = enable_bm25
        self.enable_multi_vector = enable_multi_vector
        self.enable_specialized = enable_specialized
        self.enable_cross_encoder = enable_cross_encoder
        self.enable_compression = enable_compression
        self.enable_query_expansion = enable_query_expansion
        self.enable_parent_documents = enable_parent_documents
        self.enable_freshness = enable_freshness
        self.fusion = fusion
        self.default_mode = default_mode
        self.last_trace: RetrievalTrace | None = None
        self.last_built: BuiltContext | None = None

    def retrieve(
        self,
        query: str,
        mode: str | None = None,
        filters: dict[str, Any] | None = None,
        top_k: int | None = None,
    ) -> RetrievalResult:
        mode_key = MODE_ALIASES.get((mode or self.default_mode).lower(), "hybrid")
        final_k = top_k or self.final_top_k
        original_query = query
        search_query = expand_query(query) if self.enable_query_expansion else query
        trace = RetrievalTrace(query=original_query, mode=mode_key)
        if search_query != original_query:
            trace.stages["query_expanded"] = 1

        # Plugin pre_retrieve hooks
        self._run_hooks("pre_retrieve", query=original_query, mode=mode_key)

        collect_mode = "hybrid" if mode_key == "rrf" else mode_key
        result_sets, sources = self._collect(search_query, collect_mode, filters or {}, trace)
        plugin_hits = self._plugin_search(original_query, mode_key)
        if plugin_hits:
            result_sets.append(plugin_hits)
            sources.append("plugin")
            trace.plugin_hits = len(plugin_hits)

        use_rrf = self.fusion == "rrf" or mode_key == "rrf"
        if use_rrf:
            merged = self.reranker.reciprocal_rank_fusion(*result_sets, top_k=max(final_k * 3, final_k))
            trace.stages["fusion"] = 1
        else:
            merged = self.reranker.merge(*result_sets, top_k=max(final_k * 3, final_k))
            trace.stages["fusion"] = 0
        trace.stages["fused"] = len(merged)
        trace.sources_used = sources

        if self.enable_parent_documents and merged:
            kb_docs = getattr(self.metadata_index, "kb", None)
            docs_iter = kb_docs.documents if kb_docs is not None else []
            merged = parent_document_expand(merged, docs_iter)
            trace.stages["parent_docs"] = len(merged)

        if self.enable_freshness and merged:
            merged = freshness_boost(merged)

        if self.enable_cross_encoder and merged:
            merged = self.cross_encoder.rerank(original_query, merged, top_k=final_k)
            trace.reranker = self.cross_encoder.backend
        else:
            merged = merged[:final_k]
            trace.reranker = "fusion_only"

        # optional metadata filters after ranking
        if filters:
            merged = self._apply_filters(merged, filters)[:final_k]

        built = self.context_builder.build(original_query, merged)
        self.last_built = built
        trace.compression = built.explain
        self.last_trace = trace

        self._run_hooks("post_retrieve", query=original_query, mode=mode_key, documents=merged, trace=trace)

        return RetrievalResult(
            query=original_query,
            documents=merged,
            context=built.text,
            trace=trace.as_dict(),
            built_context=built,
        )

    def _collect(
        self,
        query: str,
        mode: str,
        filters: dict[str, Any],
        trace: RetrievalTrace,
    ) -> tuple[list[list[ScoredDocument]], list[str]]:
        sets: list[list[ScoredDocument]] = []
        sources: list[str] = []

        def add(name: str, hits: list[ScoredDocument]) -> None:
            if hits:
                sets.append(hits)
                sources.append(name)
                trace.stages[name] = len(hits)

        run_all = mode == "hybrid"
        run_graph = mode in {"hybrid", "graphrag"}

        if mode in {"hybrid", "vector", "graphrag", "multi_vector"} or run_all:
            if mode != "bm25":
                add("vector", self.vector_index.search(query, top_k=self.vector_top_k))

        if (run_all or mode == "bm25") and self.enable_bm25 and self.bm25_index is not None:
            add("bm25", self.bm25_index.search(query, top_k=self.bm25_top_k))

        if run_all or mode == "metadata":
            add("metadata", self.metadata_index.search(query, top_k=self.metadata_top_k))

        if (run_all or mode == "multi_vector") and self.enable_multi_vector and self.multi_vector_index is not None:
            if self.multi_vector_index.is_indexed:
                add("multi_vector", self.multi_vector_index.search(query, top_k=self.vector_top_k))

        if self.enable_specialized:
            if run_all or mode == "sql":
                if self.sql_retriever is not None:
                    add("sql", self.sql_retriever.search(query, top_k=self.specialized_top_k))
            if run_all or mode == "code":
                if self.code_retriever is not None:
                    add("code", self.code_retriever.search(query, top_k=self.specialized_top_k))
            if run_all or mode == "api":
                if self.api_retriever is not None:
                    add("api", self.api_retriever.search(query, top_k=self.specialized_top_k))

        # GraphRAG expansion from dense + sparse + metadata seeds
        if run_graph and sets:
            seeds = [h for group in sets for h in group]
            graph_hits = self.graph_index.search_from_seeds(seeds)
            add("graph", graph_hits)
        elif mode == "graphrag":
            # pure graphrag: vector seeds then expand
            seeds = self.vector_index.search(query, top_k=self.vector_top_k)
            add("vector", seeds)
            add("graph", self.graph_index.search_from_seeds(seeds))

        return sets, sources

    def _plugin_search(self, query: str, mode: str) -> list[ScoredDocument]:
        if self.plugin_manager is None:
            return []
        hits: list[ScoredDocument] = []
        for key, handler in list(self.plugin_manager._registered.items()):
            if not key.startswith("search:"):
                continue
            try:
                result = handler(query=query, mode=mode, brain_pipeline=self)
            except TypeError:
                try:
                    result = handler(query)
                except Exception:
                    continue
            except Exception:
                continue
            if not result:
                continue
            for item in result:
                if isinstance(item, ScoredDocument):
                    hits.append(item)
        return hits

    def _run_hooks(self, hook: str, **kwargs: Any) -> None:
        if self.plugin_manager is None:
            return
        prefix = f"event:{hook}"
        for key, handler in list(self.plugin_manager._registered.items()):
            if key == prefix or key.startswith(prefix + ":"):
                try:
                    handler(**kwargs)
                except TypeError:
                    try:
                        handler(kwargs)
                    except Exception:
                        pass
                except Exception:
                    pass

    @staticmethod
    def _apply_filters(docs: list[ScoredDocument], filters: dict[str, Any]) -> list[ScoredDocument]:
        out = docs
        if "doc_type" in filters:
            allowed = set(filters["doc_type"] if isinstance(filters["doc_type"], list) else [filters["doc_type"]])
            out = [s for s in out if s.document.doc_type in allowed]
        if "category" in filters:
            allowed = set(filters["category"] if isinstance(filters["category"], list) else [filters["category"]])
            out = [s for s in out if s.document.category in allowed]
        if "hub" in filters:
            allowed = set(filters["hub"] if isinstance(filters["hub"], list) else [filters["hub"]])
            out = [s for s in out if s.document.hub in allowed]
        return out

    def capabilities(self) -> dict[str, Any]:
        return {
            "vector_rag": True,
            "graphrag": True,
            "hybrid_retrieval": True,
            "bm25_search": bool(self.bm25_index is not None and self.enable_bm25),
            "metadata_search": True,
            "sql_retrieval": self.sql_retriever is not None,
            "code_retrieval": self.code_retriever is not None,
            "api_retrieval": self.api_retriever is not None,
            "multi_vector_retrieval": self.multi_vector_index is not None,
            "cross_encoder_reranking": self.enable_cross_encoder,
            "context_compression": self.enable_compression,
            "context_builder": True,
            "explainable_retrieval": True,
            "incremental_indexing": True,
            "query_expansion": self.enable_query_expansion,
            "parent_document_retrieval": self.enable_parent_documents,
            "freshness_boost": self.enable_freshness,
            "reciprocal_rank_fusion": True,
            "plugin_system": self.plugin_manager is not None,
            "modes": sorted(set(MODE_ALIASES.values())),
            "cross_encoder_backend": self.cross_encoder.backend if self.cross_encoder else None,
            "fusion": self.fusion,
        }
