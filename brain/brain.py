"""
Coltex RAG database engine.

Knowledge base · vector index · metadata · graph relationships · retrieval pipeline.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from brain.embeddings.encoder import EmbeddingEncoder
from brain.graph.relationships import GraphIndex
from brain.indexing.vector_index import VectorIndex
from brain.ingestion.loader import KnowledgeBase
from brain.metadata.index import MetadataIndex
from brain.reranking.reranker import Reranker
from brain.retrieval.pipeline import RetrievalPipeline
from brain.types import RetrievalResult


class Coltex:
    """
    Coltex RAG database engine:
    - Knowledge Base (documents)
    - Vector Database (embeddings)
    - Metadata Index
    - Graph Relationships
    - Retrieval Pipeline
    """

    def __init__(self, config: dict[str, Any] | None = None, config_path: str | Path = "config/brain.yaml"):
        self.config = config or self._load_config(config_path)
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

        gr_cfg = self.config.get("graph", {})
        self.graph_index = GraphIndex(
            self.kb,
            max_hops=int(gr_cfg.get("max_hops", 2)),
            max_extra=int(gr_cfg.get("max_extra_chunks", 8)),
            advanced_routing=bool(gr_cfg.get("advanced_routing", False)),
        )

        ret_cfg = self.config.get("retrieval", {})
        self.retrieval = RetrievalPipeline(
            vector_index=self.vector_index,
            metadata_index=self.metadata_index,
            graph_index=self.graph_index,
            reranker=Reranker(ret_cfg.get("source_weights")),
            vector_top_k=int(ret_cfg.get("vector_top_k", 10)),
            metadata_top_k=int(ret_cfg.get("metadata_top_k", 8)),
            final_top_k=int(ret_cfg.get("final_top_k", 8)),
            max_context_chars=int(ret_cfg.get("max_context_chars", 14000)),
        )

    def index(self, force: bool = False) -> int:
        if force:
            import shutil
            if self.vector_index.persist_dir.exists():
                shutil.rmtree(self.vector_index.persist_dir)
            self.vector_index._collection = None
            self.vector_index._client = None
        if force or not self.vector_index.is_indexed:
            return self.vector_index.index()
        self.vector_index._connect()
        return self.vector_index._collection.count()

    def retrieve(self, query: str) -> RetrievalResult:
        return self.retrieval.retrieve(query)

    def index_document(self, doc) -> None:
        """Index a single document without full rebuild."""
        self.metadata_index.refresh()
        self.vector_index.index_document(doc)

    @property
    def document_count(self) -> int:
        return len(self.kb)

    def stats(self) -> dict[str, Any]:
        indexed = 0
        try:
            indexed = self.vector_index._collection.count() if self.vector_index._collection else 0
        except Exception:
            pass
        return {
            "documents": len(self.kb),
            "indexed_vectors": indexed,
            "vector_store": str(self.vector_index.persist_dir),
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
            if "/lobes/" in path:
                cluster = path.split("/lobes/")[1].split("/")[0]
                clusters[cluster] = clusters.get(cluster, 0) + 1
            if "/memory/" in path:
                tier = path.split("/memory/")[1].split("/")[0]
                memory_tiers[tier] = memory_tiers.get(tier, 0) + 1
            for part in path.split("/"):
                if part.startswith("L") and "-" in part and "/cortex/" in path:
                    processing_layers[part] = processing_layers.get(part, 0) + 1
            if "/synapses/" in path:
                graph_links += 1
            if "/pathways/" in path:
                pathways += 1
            if "/reflexes/" in path:
                quick_reference += 1
            if doc.hub:
                hubs[doc.hub] = hubs.get(doc.hub, 0) + 1
            edges += len(doc.related) + sum(len(v) for v in doc.relationships.values())

        neural_map_path = Path("data/brain/neural-map.json")
        arch_path = Path("data/brain/architecture-manifest.json")
        neural_map: dict = {}
        arch_manifest: dict = {}
        if neural_map_path.exists():
            import json
            try:
                neural_map = json.loads(neural_map_path.read_text(encoding="utf-8"))
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
                "pathways": pathways,
                "quick_reference": quick_reference,
                "graph_edges": edges,
                "graph_density": round(edges / max(base["documents"], 1), 2),
                "catalog_index": neural_map_path.exists(),
                "architecture_manifest": arch_path.exists(),
                "catalog_summary": {
                    "total_documents": neural_map.get("total_documents"),
                    "pathways": neural_map.get("pathways"),
                    "hubs_registered": neural_map.get("hubs_registered"),
                } if neural_map else None,
            },
        }

    def pulse(self) -> dict[str, Any]:
        """Deprecated alias for report()."""
        return self.report()
