"""`.ctex` workspace manifest read/write."""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from runtime.workspace.context import COLTEX_VERSION, WorkspaceContext

MANIFEST_FORMAT = "coltex-workspace"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def default_manifest(name: str) -> dict[str, Any]:
    return {
        "format": MANIFEST_FORMAT,
        "version": "1.0",
        "name": name,
        "uuid": str(uuid.uuid4()),
        "coltex_version": COLTEX_VERSION,
        "created_at": _now_iso(),
        "modified_at": _now_iso(),
        "paths": {
            "knowledge": "knowledge",
            "documents": "documents",
            "embeddings": "embeddings",
            "graph": "graph",
            "metadata": "metadata",
            "cache": "cache",
            "indexes": "indexes",
            "logs": "logs",
            "backups": "backups",
            "settings": "settings",
            "runtime": "runtime",
        },
        "sources": [],
        "runtime": {
            "event_log": "runtime/events.jsonl",
            "brain_config": "settings/brain.yaml",
        },
        "ai": {
            "provider": "local",
            "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
        },
        "retrieval": {
            "vector_top_k": 15,
            "metadata_top_k": 12,
            "final_top_k": 12,
            "max_context_chars": 20000,
            "chunk_size": 2000,
        },
        "graph": {
            "enabled": True,
            "max_hops": 4,
        },
        "search": {
            "modes": ["documents", "metadata", "code", "api", "sql"],
        },
        "statistics": {
            "documents": 0,
            "embeddings": 0,
            "graph_nodes": 0,
            "sources": 0,
            "last_build_at": None,
            "workspace_size_bytes": 0,
        },
        "plugins": [],
        "health": {
            "knowledge_score": 0,
            "status": "new",
        },
        "settings": {
            "workspace": name,
            "backup_enabled": False,
        },
    }


def load_manifest(manifest_path: Path) -> dict[str, Any]:
    text = manifest_path.read_text(encoding="utf-8")
    data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise ValueError(f"Invalid .ctex manifest: {manifest_path}")
    if data.get("format") != MANIFEST_FORMAT:
        raise ValueError(f"Not a Coltex workspace manifest: {manifest_path}")
    return data


def save_manifest(manifest_path: Path, data: dict[str, Any]) -> None:
    data["modified_at"] = _now_iso()
    manifest_path.write_text(
        yaml.dump(data, default_flow_style=False, sort_keys=False),
        encoding="utf-8",
    )


def sync_manifest_from_runtime(ctx: WorkspaceContext, runtime) -> dict[str, Any]:
    """Refresh manifest statistics and health from live runtime state."""
    data = load_manifest(ctx.manifest_path)
    brain = runtime.brain.stats()
    health = runtime.analytics.health()
    graph = runtime.graph.stats()
    sources = runtime.sources.count()

    data["statistics"] = {
        "documents": brain.get("documents", 0),
        "embeddings": brain.get("indexed_vectors", 0),
        "graph_nodes": graph.get("graph_edges", 0) + brain.get("documents", 0),
        "sources": sources,
        "last_build_at": data.get("statistics", {}).get("last_build_at"),
        "workspace_size_bytes": ctx.dir_size_bytes(),
    }
    data["health"] = {
        "knowledge_score": health.get("knowledge_score", 0),
        "status": "ready" if brain.get("documents", 0) else "empty",
    }
    data["ai"]["embedding_model"] = runtime.settings.load().get(
        "embedding_model", data["ai"].get("embedding_model")
    )
    data["settings"] = {**data.get("settings", {}), **runtime.settings.load()}
    data["sources"] = _collect_sources(runtime)
    save_manifest(ctx.manifest_path, data)
    return data


def _collect_sources(runtime) -> list[dict[str, Any]]:
    return [
        {"name": s["name"], "path": s["path"], "status": s["status"]}
        for s in runtime.sources.list_sources()[:100]
    ]


def export_metadata_snapshot(ctx: WorkspaceContext, runtime) -> None:
    """Write lightweight metadata and graph snapshots into workspace folders."""
    docs = []
    for doc in runtime.brain.kb.documents:
        docs.append({
            "id": doc.doc_id,
            "title": doc.title,
            "path": doc.path,
            "doc_type": doc.doc_type,
            "hub": doc.hub,
            "tags": doc.tags,
        })
    meta_path = ctx.metadata / "documents.json"
    meta_path.write_text(json.dumps({"documents": docs, "count": len(docs)}, indent=2), encoding="utf-8")

    edges = []
    for doc in runtime.brain.kb.documents:
        for edge_type, targets in doc.relationships.items():
            for target in targets:
                edges.append({"from": doc.doc_id, "type": edge_type, "to": target})
        for rel in doc.related or []:
            edges.append({"from": doc.doc_id, "type": "related", "to": rel})
    graph_path = ctx.graph / "edges.json"
    graph_path.write_text(json.dumps({"edges": edges, "count": len(edges)}, indent=2), encoding="utf-8")
