"""Workspace path layout and resolution."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

COLTEX_VERSION = "1.0.0"

WORKSPACE_DIRS = (
    "knowledge",
    "documents",
    "embeddings",
    "graph",
    "metadata",
    "cache",
    "indexes",
    "logs",
    "backups",
    "settings",
    "runtime",
)

DOCUMENT_SUBDIRS = ("inbox", "processed")


@dataclass
class WorkspaceContext:
    """Resolved paths for a Coltex `.ctex` workspace."""

    root: Path
    manifest_path: Path
    name: str

    @classmethod
    def from_manifest(cls, manifest_path: Path) -> WorkspaceContext:
        manifest_path = manifest_path.resolve()
        if manifest_path.suffix != ".ctex":
            raise ValueError(f"Expected a .ctex manifest file: {manifest_path}")
        root = manifest_path.parent
        data = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
        name = str(data.get("name") or root.name)
        return cls(root=root, manifest_path=manifest_path, name=name)

    @property
    def knowledge(self) -> Path:
        return self.root / "knowledge"

    @property
    def documents(self) -> Path:
        return self.root / "documents"

    @property
    def documents_inbox(self) -> Path:
        return self.documents / "inbox"

    @property
    def documents_processed(self) -> Path:
        return self.documents / "processed"

    @property
    def embeddings(self) -> Path:
        return self.root / "embeddings"

    @property
    def vector_store(self) -> Path:
        return self.embeddings / "vector_store"

    @property
    def graph(self) -> Path:
        return self.root / "graph"

    @property
    def metadata(self) -> Path:
        return self.root / "metadata"

    @property
    def cache(self) -> Path:
        return self.root / "cache"

    @property
    def indexes(self) -> Path:
        return self.root / "indexes"

    @property
    def logs(self) -> Path:
        return self.root / "logs"

    @property
    def backups(self) -> Path:
        return self.root / "backups"

    @property
    def settings_dir(self) -> Path:
        return self.root / "settings"

    @property
    def runtime_dir(self) -> Path:
        return self.root / "runtime"

    @property
    def brain_config_path(self) -> Path:
        return self.settings_dir / "brain.yaml"

    @property
    def settings_json_path(self) -> Path:
        return self.settings_dir / "workspace.json"

    @property
    def event_log_path(self) -> Path:
        return self.runtime_dir / "events.jsonl"

    @property
    def usage_path(self) -> Path:
        return self.runtime_dir / "usage.json"

    def ensure_layout(self) -> None:
        for name in WORKSPACE_DIRS:
            (self.root / name).mkdir(parents=True, exist_ok=True)
        for sub in DOCUMENT_SUBDIRS:
            (self.documents / sub).mkdir(parents=True, exist_ok=True)
        self.vector_store.mkdir(parents=True, exist_ok=True)

    def write_brain_config(self, settings: dict[str, Any] | None = None) -> None:
        settings = settings or {}
        embedding_model = settings.get(
            "embedding_model", "sentence-transformers/all-MiniLM-L6-v2"
        )
        chunk_size = int(settings.get("chunk_size", 2000))
        cfg = {
            "knowledge_base": {
                "paths": [str(self.knowledge)],
                "glob": "**/*.md",
                "exclude": ["**/cache/**"],
            },
            "embeddings": {"model": embedding_model},
            "vector_store": {
                "persist_dir": str(self.vector_store),
                "collection_name": "coltex",
            },
            "graph": {
                "enabled": True,
                "advanced_routing": True,
                "max_hops": 4,
                "max_extra_chunks": 16,
            },
            "retrieval": {
                "vector_top_k": 15,
                "metadata_top_k": 12,
                "final_top_k": 12,
                "max_context_chars": 20000,
                "chunk_size": chunk_size,
            },
            "search": {
                "modes": ["documents", "metadata", "code", "api", "sql"],
            },
        }
        self.brain_config_path.write_text(
            yaml.dump(cfg, default_flow_style=False, sort_keys=False),
            encoding="utf-8",
        )

    def load_brain_config(self) -> dict[str, Any]:
        if not self.brain_config_path.exists():
            self.write_brain_config()
        return yaml.safe_load(self.brain_config_path.read_text(encoding="utf-8")) or {}

    def relative(self, path: Path) -> str:
        try:
            return str(path.resolve().relative_to(self.root.resolve()))
        except ValueError:
            return str(path)

    def dir_size_bytes(self) -> int:
        total = 0
        for path in self.root.rglob("*"):
            if path.is_file():
                try:
                    total += path.stat().st_size
                except OSError:
                    pass
        return total
