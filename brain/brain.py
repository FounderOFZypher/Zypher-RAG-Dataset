"""
Coltex RAG database engine.

Advanced hybrid retrieval:
  Vector RAG · GraphRAG · BM25 · Metadata · SQL · Code · API
  Multi-Vector · Cross-Encoder · Context Compression · Incremental Indexing
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from brain.embeddings.encoder import EmbeddingEncoder
from brain.graph.relationships import GraphIndex
from brain.indexing.bm25_index import BM25Index
from brain.indexing.incremental import IncrementalIndexer
from brain.indexing.multi_vector_index import MultiVectorIndex
from brain.indexing.vector_index import VectorIndex
from brain.ingestion.loader import KnowledgeBase
from brain.metadata.index import MetadataIndex
from brain.reranking.cross_encoder import CrossEncoderReranker
from brain.reranking.reranker import Reranker
from brain.retrieval.context import ContextBuilder
from brain.retrieval.pipeline import RetrievalPipeline
from brain.retrieval.specialized import APIRetriever, CodeRetriever, SQLRetriever
from brain.types import RetrievalResult


class Coltex:
    """
    Coltex Mega RAG engine with advanced retrieval capabilities.
    """

    def __init__(
        self,
        config: dict[str, Any] | None = None,
        config_path: str | Path = "config/brain.yaml",
        plugin_manager=None,
    ):
        self.config = config or self._load_config(config_path)
        self.plugin_manager = plugin_manager
        self._init_components()

    @staticmethod
    def _load_config(path: str | Path) -> dict[str, Any]:
        with Path(path).open(encoding="utf-8") as f:
            return yaml.safe_load(f)

    def _init_components(self) -> None:
        kb_cfg = self.config["knowledge_base"]
        self.kb = KnowledgeBase(
            paths=kb_cfg["paths"],
            glob_pattern=kb_cfg.get("glob", "**/*.md"),
            exclude=kb_cfg.get("exclude"),
        )

        emb_cfg = self.config.get("embeddings", {})
        self.encoder = EmbeddingEncoder(emb_cfg.get("model", "sentence-transformers/all-MiniLM-L6-v2"))

        vs_cfg = self.config.get("vector_store", {})
        self.vector_index = VectorIndex(
            self.kb,
            self.encoder,
            persist_dir=vs_cfg.get("persist_dir", "data/brain/vector_store"),
            collection_name=vs_cfg.get("collection_name", "coltex"),
        )

        self.metadata_index = MetadataIndex(self.kb)

        ret_cfg = self.config.get("retrieval", {})
        adv = ret_cfg.get("advanced", {})

        self.bm25_index = BM25Index(self.kb) if adv.get("bm25", True) else None

        mv_cfg = vs_cfg.get("multi_vector", {})
        self.multi_vector_index = None
        if adv.get("multi_vector", True):
            self.multi_vector_index = MultiVectorIndex(
                self.kb,
                self.encoder,
                persist_dir=mv_cfg.get("persist_dir", "data/brain/multi_vector_store"),
                collection_name=mv_cfg.get("collection_name", "coltex_multivec"),
            )

        self.sql_retriever = SQLRetriever(self.kb) if adv.get("sql_retrieval", True) else None
        self.code_retriever = CodeRetriever(self.kb) if adv.get("code_retrieval", True) else None
        self.api_retriever = APIRetriever(self.kb) if adv.get("api_retrieval", True) else None

        gr_cfg = self.config.get("graph", {})
        self.graph_index = GraphIndex(
            self.kb,
            max_hops=int(gr_cfg.get("max_hops", 2)),
            max_extra=int(gr_cfg.get("max_extra_chunks", 8)),
            advanced_routing=bool(gr_cfg.get("advanced_routing", False)),
        )

        ce_cfg = adv.get("cross_encoder", {})
        cross_encoder = CrossEncoderReranker(
            model_name=ce_cfg.get("model", "cross-encoder/ms-marco-MiniLM-L-6-v2"),
            enabled=bool(adv.get("cross_encoder_reranking", True)),
        )

        context_builder = ContextBuilder(
            max_chars=int(ret_cfg.get("max_context_chars", 14000)),
            per_doc_chars=int(adv.get("per_doc_chars", 2500)),
            compress=bool(adv.get("context_compression", True)),
            diversity=bool(adv.get("context_diversity", True)),
        )

        self.retrieval = RetrievalPipeline(
            vector_index=self.vector_index,
            metadata_index=self.metadata_index,
            graph_index=self.graph_index,
            bm25_index=self.bm25_index,
            multi_vector_index=self.multi_vector_index,
            sql_retriever=self.sql_retriever,
            code_retriever=self.code_retriever,
            api_retriever=self.api_retriever,
            reranker=Reranker(ret_cfg.get("source_weights")),
            cross_encoder=cross_encoder,
            context_builder=context_builder,
            plugin_manager=self.plugin_manager,
            vector_top_k=int(ret_cfg.get("vector_top_k", 10)),
            metadata_top_k=int(ret_cfg.get("metadata_top_k", 8)),
            bm25_top_k=int(ret_cfg.get("bm25_top_k", 15)),
            specialized_top_k=int(ret_cfg.get("specialized_top_k", 10)),
            final_top_k=int(ret_cfg.get("final_top_k", 8)),
            max_context_chars=int(ret_cfg.get("max_context_chars", 14000)),
            enable_bm25=bool(adv.get("bm25", True)),
            enable_multi_vector=bool(adv.get("multi_vector", True)),
            enable_specialized=bool(adv.get("specialized", True)),
            enable_cross_encoder=bool(adv.get("cross_encoder_reranking", True)),
            enable_compression=bool(adv.get("context_compression", True)),
            default_mode=str(ret_cfg.get("default_mode", "hybrid")),
            source_weights=ret_cfg.get("source_weights"),
            enable_query_expansion=bool(adv.get("query_expansion", True)),
            enable_parent_documents=bool(adv.get("parent_document_retrieval", True)),
            enable_freshness=bool(adv.get("freshness_boost", True)),
            fusion=str(adv.get("fusion", "weighted")),
        )

        self.incremental = IncrementalIndexer(
            vector_index=self.vector_index,
            multi_vector_index=self.multi_vector_index,
            bm25_index=self.bm25_index,
            metadata_index=self.metadata_index,
            specialized=[x for x in (self.sql_retriever, self.code_retriever, self.api_retriever) if x],
        )

    def index(self, force: bool = False, multi_vector: bool | None = None) -> dict[str, int]:
        if force:
            import shutil
            if self.vector_index.persist_dir.exists():
                shutil.rmtree(self.vector_index.persist_dir)
            self.vector_index._collection = None
            self.vector_index._client = None
            if self.multi_vector_index is not None and self.multi_vector_index.persist_dir.exists():
                shutil.rmtree(self.multi_vector_index.persist_dir)
                self.multi_vector_index._collection = None
                self.multi_vector_index._client = None

        counts: dict[str, int] = {}
        if force or not self.vector_index.is_indexed:
            counts["vector"] = self.vector_index.index()
        else:
            self.vector_index._connect()
            counts["vector"] = self.vector_index._collection.count()

        if self.bm25_index is not None:
            self.bm25_index.refresh()
            counts["bm25"] = len(self.bm25_index._docs)

        do_mv = self.multi_vector_index is not None and (
            multi_vector if multi_vector is not None else self.config.get("retrieval", {}).get("advanced", {}).get("index_multi_vector_on_build", False)
        )
        if do_mv and self.multi_vector_index is not None:
            if force or not self.multi_vector_index.is_indexed:
                max_docs = self.config.get("retrieval", {}).get("advanced", {}).get("multi_vector_max_docs")
                counts["multi_vector"] = self.multi_vector_index.index(max_docs=max_docs)
            else:
                counts["multi_vector"] = self.multi_vector_index._collection.count()

        for name, retriever in (
            ("sql", self.sql_retriever),
            ("code", self.code_retriever),
            ("api", self.api_retriever),
        ):
            if retriever is not None:
                retriever.refresh()
                counts[name] = len(retriever._pool)

        self.metadata_index.refresh()
        counts["metadata"] = len(self.kb)
        return counts

    def retrieve(
        self,
        query: str,
        mode: str | None = None,
        filters: dict[str, Any] | None = None,
        top_k: int | None = None,
    ) -> RetrievalResult:
        return self.retrieval.retrieve(query, mode=mode, filters=filters, top_k=top_k)

    def index_document(self, doc) -> dict[str, Any]:
        """Incrementally index a single document across all backends."""
        # ensure KB sees the document if newly added externally
        if doc.doc_id not in {d.doc_id for d in self.kb.documents}:
            self.kb.documents.append(doc)
        report = self.incremental.upsert(doc)
        return report.as_dict()

    def delete_document(self, doc_id: str) -> dict[str, Any]:
        """Incrementally remove a document from indexes."""
        self.kb.documents = [d for d in self.kb.documents if d.doc_id != doc_id]
        report = self.incremental.delete(doc_id)
        return report.as_dict()

    def capabilities(self) -> dict[str, Any]:
        caps = self.retrieval.capabilities()
        caps["multi_workspace"] = True
        caps["incremental_indexing"] = True
        return caps

    @property
    def document_count(self) -> int:
        return len(self.kb)

    def stats(self) -> dict[str, Any]:
        indexed = 0
        try:
            indexed = self.vector_index._collection.count() if self.vector_index._collection else 0
        except Exception:
            pass
        mv = 0
        try:
            if self.multi_vector_index is not None and self.multi_vector_index._collection is not None:
                mv = self.multi_vector_index._collection.count()
        except Exception:
            pass
        return {
            "documents": len(self.kb),
            "indexed_vectors": indexed,
            "multi_vectors": mv,
            "bm25_docs": len(self.bm25_index._docs) if self.bm25_index else 0,
            "vector_store": str(self.vector_index.persist_dir),
            "capabilities": self.capabilities(),
        }

    def report(self) -> dict[str, Any]:
        """Corpus architecture report — document counts, graph density, catalog summary."""
        base = self.stats()
        domains: dict[str, int] = {}
        hubs: dict[str, int] = {}
        clusters: dict[str, int] = {}
        memory_tiers: dict[str, int] = {}
        processing_layers: dict[str, int] = {}
        graph_links = pathways = quick_reference = 0
        edges = 0

        for doc in self.kb.documents:
            path = doc.path.replace("\\", "/")
            if "/domains/" in path:
                cat = path.split("/domains/")[1].split("/")[0]
                domains[cat] = domains.get(cat, 0) + 1
            if "/clusters/" in path:
                cluster = path.split("/clusters/")[1].split("/")[0]
                clusters[cluster] = clusters.get(cluster, 0) + 1
            for standalone in ("automation", "operations", "retention", "routing", "priority"):
                if f"/{standalone}/" in path:
                    clusters[standalone] = clusters.get(standalone, 0) + 1
            if "/memory/" in path:
                tier = path.split("/memory/")[1].split("/")[0]
                memory_tiers[tier] = memory_tiers.get(tier, 0) + 1
            for part in path.split("/"):
                if part.startswith("L") and "-" in part and "/processing-layers/" in path:
                    processing_layers[part] = processing_layers.get(part, 0) + 1
            if "/graph-links/" in path:
                graph_links += 1
            if "/domain-routes/" in path:
                pathways += 1
            if "/quick-reference/" in path:
                quick_reference += 1
            if doc.hub:
                hubs[doc.hub] = hubs.get(doc.hub, 0) + 1
            edges += len(doc.related) + sum(len(v) for v in doc.relationships.values())

        catalog_path = Path("data/brain/catalog-index.json")
        arch_path = Path("data/brain/architecture-manifest.json")
        catalog: dict = {}
        arch_manifest: dict = {}
        if catalog_path.exists():
            import json
            try:
                catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                pass
        if arch_path.exists():
            import json
            try:
                arch_manifest = json.loads(arch_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                pass

        return {
            **base,
            "architecture": {
                "status": "active" if base["documents"] > 0 else "empty",
                "version": arch_manifest.get("version", "2.0"),
                "advanced_routing": self.config.get("graph", {}).get("advanced_routing", False),
                "domains": domains,
                "domain_count": len(domains),
                "clusters": clusters,
                "cluster_count": len(clusters),
                "hubs": hubs,
                "hub_count": len(hubs),
                "memory_tiers": memory_tiers,
                "processing_layers": processing_layers,
                "graph_links": graph_links,
                "domain_routes": pathways,
                "quick_reference": quick_reference,
                "graph_edges": edges,
                "graph_density": round(edges / max(base["documents"], 1), 2),
                "catalog_index": catalog_path.exists(),
                "architecture_manifest": arch_path.exists(),
                "catalog_summary": {
                    "total_documents": catalog.get("total_documents"),
                    "domain_routes": catalog.get("domain_routes"),
                    "hubs_registered": catalog.get("hubs_registered"),
                } if catalog else None,
            },
        }
