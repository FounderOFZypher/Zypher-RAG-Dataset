"""
Coltex Runtime — Mega RAG corpus runtime and CLI.

Orchestrates intelligence, search, memory, graph, retrieval, events,
scheduler, plugins, curator, analytics, and workspace management.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from brain.brain import Coltex
from runtime.api.gateway import APIGateway
from runtime.connectors.base import ConnectorRegistry
from runtime.connectors.filesystem import FilesystemConnector
from runtime.connectors.github import GitHubConnector
from runtime.engines.analytics import AnalyticsEngine
from runtime.engines.curator import CuratorEngine
from runtime.engines.explain import ExplainEngine
from runtime.engines.graph import GraphEngine
from runtime.engines.intelligence import IntelligenceEngine
from runtime.engines.memory import MemoryEngine
from runtime.engines.retrieval import RetrievalEngine
from runtime.engines.scheduler import SchedulerEngine
from runtime.engines.search import SearchEngine
from runtime.events.bus import EventBus
from runtime.knowledge.dna import KnowledgeDNA
from runtime.monitoring.metrics import RuntimeMonitor
from runtime.plugins import sdk as plugin_sdk
from runtime.plugins.manager import PluginManager
from runtime.security.gateway import SecurityGateway
from runtime.ask.knowledge import AskKnowledge
from runtime.processing.pipeline import ProcessingPipeline
from runtime.sources.upload import SourceManager
from runtime.studio.studio import ColtexCLI
from runtime.v1.dashboard import V1Dashboard
from runtime.v1.settings import SettingsStore
from runtime.workspace.context import WorkspaceContext
from runtime.workspace.manifest import sync_manifest_from_runtime

ROOT = Path(__file__).resolve().parent.parent


class ColtexRuntime:
    """Coltex Runtime — local CLI with optional `.ctex` workspace."""

    def __init__(
        self,
        config_path: str | Path = "config/runtime.yaml",
        workspace: WorkspaceContext | None = None,
    ):
        self.workspace = workspace
        self.config_path = Path(config_path)
        if not self.config_path.is_absolute():
            self.config_path = ROOT / self.config_path
        self.config = self._load_config()

        if workspace is not None:
            workspace.ensure_layout()
            self.data_dir = workspace.runtime_dir
            self.data_dir.mkdir(parents=True, exist_ok=True)
            brain_config = workspace.load_brain_config()
            self.plugins = PluginManager()
            plugin_sdk.init(self.plugins)
            self.brain = Coltex(config=brain_config, plugin_manager=self.plugins)
            log_path = workspace.event_log_path
            events_cfg = ROOT / self.config.get("events_config", "config/events.yaml")
        else:
            self.data_dir = ROOT / self.config.get("runtime", {}).get("data_dir", "data/runtime")
            self.data_dir.mkdir(parents=True, exist_ok=True)
            brain_cfg = self.config.get("brain_config", "config/brain.yaml")
            self.plugins = PluginManager()
            plugin_sdk.init(self.plugins)
            self.brain = Coltex(
                config_path=ROOT / brain_cfg if not Path(brain_cfg).is_absolute() else brain_cfg,
                plugin_manager=self.plugins,
            )
            log_path = self.config.get("runtime", {}).get("event_log", "data/runtime/events.jsonl")
            events_cfg = self.config.get("events_config", "config/events.yaml")

        self.event_bus = EventBus(config_path=events_cfg, log_path=log_path)

        self.settings = SettingsStore(workspace=workspace)
        self.sources = SourceManager(workspace=workspace)
        self.processing = ProcessingPipeline(self)

        self.monitor = RuntimeMonitor(self)
        self.intelligence = IntelligenceEngine(self.brain, self.event_bus)
        self.search = SearchEngine(self.brain)
        self.memory = MemoryEngine(self.brain)
        self.scheduler = SchedulerEngine()
        self.retrieval = RetrievalEngine(self.brain)
        self.graph = GraphEngine(self.brain)
        self.curator = CuratorEngine(self.brain, self.event_bus, self.data_dir)
        self.analytics = AnalyticsEngine(self.brain)
        self.explain = ExplainEngine(self.brain, self.monitor)
        self.security = SecurityGateway()
        self.api = APIGateway(self)
        self.studio = ColtexCLI(self)
        self.ask = AskKnowledge(self)
        self.v1 = V1Dashboard(self)

        from runtime.engines.multi_workspace import MultiWorkspaceSearch
        self.multi_workspace = MultiWorkspaceSearch()
        if workspace is not None:
            try:
                self.multi_workspace.add_workspace(workspace.manifest_path)
            except Exception:
                pass

        self.connectors = ConnectorRegistry()
        self.connectors.register(FilesystemConnector())
        self.connectors.register(GitHubConnector())

        self._wire_default_subscribers()
        if workspace is not None:
            self.sync_workspace_manifest()

    @staticmethod
    def _load_config(path: Path | None = None) -> dict[str, Any]:
        cfg_path = path or ROOT / "config/runtime.yaml"
        with cfg_path.open(encoding="utf-8") as f:
            return yaml.safe_load(f)

    @classmethod
    def from_active_workspace(cls, config_path: str | Path = "config/runtime.yaml") -> ColtexRuntime:
        from runtime.workspace.session import get_active_workspace

        manifest = get_active_workspace()
        if manifest is None:
            return cls(config_path=config_path)
        ctx = WorkspaceContext.from_manifest(manifest)
        return cls(config_path=config_path, workspace=ctx)

    def sync_workspace_manifest(self) -> None:
        if self.workspace is not None:
            sync_manifest_from_runtime(self.workspace, self)

    def _wire_default_subscribers(self) -> None:
        def on_pipeline_complete(event):
            if event.id == "analytics.updated":
                self.curator.proactive_scan(save=True)
                self.sync_workspace_manifest()

        self.event_bus.subscribe("analytics.updated", on_pipeline_complete)

    def status(self) -> dict[str, Any]:
        base = {
            "runtime": "coltex-runtime",
            "version": self.config.get("version", "1.0.0"),
            "platform": "Coltex V1 CLI",
            "interface": "cli",
            "commands": {
                "new": "coltex new MyWorkspace",
                "open": "coltex open MyWorkspace.ctex",
                "build": "coltex build",
                "status": "coltex status",
                "validate": "coltex validate",
                "upload": "coltex upload file.pdf",
                "ask": "coltex ask \"your question\"",
                "search": "coltex search \"query\"",
            },
            "coltex_v1": {
                "tagline": "Commercial RAG corpus — 100,000,000+ documents",
                "goal": "AI-ready intelligence in under 10 minutes",
                "docs": "docs/product/coltex-v1.md",
                "license": "MIT",
            },
            "capabilities": self.capabilities(),
            "engines": {
                "intelligence": self.intelligence.stats(),
                "search": self.search.stats(),
                "memory": self.memory.stats(),
                "scheduler": self.scheduler.stats(),
                "event_bus": self.event_bus.stats(),
                "plugins": self.plugins.stats(),
                "retrieval": self.retrieval.stats(),
                "graph": self.graph.stats(),
                "curator": self.curator.stats(),
                "analytics": self.analytics.stats(),
                "monitor": {"status": "active"},
                "explain": {"status": "active"},
                "security": self.security.stats(),
            },
        }
        if self.workspace is not None:
            base["workspace"] = {
                "name": self.workspace.name,
                "manifest": str(self.workspace.manifest_path),
                "root": str(self.workspace.root),
            }
        return base

    def workspace_status(self) -> dict[str, Any]:
        """Workspace-focused status for `coltex status`."""
        if self.workspace is None:
            return {"error": "no active workspace", "hint": "Run `coltex new <name>` or `coltex open <file.ctex>`"}

        self.sync_workspace_manifest()
        from runtime.workspace.manifest import load_manifest

        data = load_manifest(self.workspace.manifest_path)
        brain = self.brain.stats()
        health = self.analytics.health()
        graph = self.graph.stats()

        return {
            "workspace": self.workspace.name,
            "manifest": str(self.workspace.manifest_path),
            "coltex_version": data.get("coltex_version"),
            "uuid": data.get("uuid"),
            "created_at": data.get("created_at"),
            "modified_at": data.get("modified_at"),
            "documents": brain.get("documents", 0),
            "embeddings": brain.get("indexed_vectors", 0),
            "graph_nodes": graph.get("graph_edges", 0) + brain.get("documents", 0),
            "knowledge_health": health.get("knowledge_score", 0),
            "last_build_at": data.get("statistics", {}).get("last_build_at"),
            "workspace_size_bytes": self.workspace.dir_size_bytes(),
            "settings": self.settings.load(),
        }

    def ingest(self, document_id: str, source: str = "upload") -> dict[str, Any]:
        if not self.security.authorize("ingest"):
            return {"error": "unauthorized"}
        payload = {"document_id": document_id, "source": source}
        events = self.event_bus.run_pipeline(payload)
        curator = self.curator.proactive_scan(save=True)
        self.sync_workspace_manifest()
        return {
            "document_id": document_id,
            "pipeline_events": [e.id for e in events],
            "subscribers_notified": True,
            "curator_alerts": curator.get("alert_count", 0),
        }

    def sync_connector(self, connector_id: str) -> dict[str, Any]:
        result = self.connectors.sync(connector_id)
        if "ingest_payloads" in result:
            for item in result["ingest_payloads"][:5]:
                self.ingest(item["document_id"], source=connector_id)
        self.sync_workspace_manifest()
        return result

    def knowledge_dna(self, document_id: str) -> dict[str, Any]:
        for doc in self.brain.kb.documents:
            if doc.doc_id == document_id:
                dna = KnowledgeDNA.from_document(doc)
                data = dna.to_dict()
                data["memory_tier"] = self.memory.resolve_tier(doc)
                data["evolution_state"] = self.memory.evolution_state(doc)
                return data
        return {"error": "not_found", "document_id": document_id}

    def universal_search(
        self,
        query: str,
        mode: str | None = None,
        filters: dict[str, Any] | None = None,
        top_k: int | None = None,
        explain: bool = False,
    ) -> dict[str, Any]:
        return self.search.search(query, mode=mode, filters=filters, top_k=top_k, explain=explain)

    def federated_search(
        self,
        query: str,
        mode: str | None = "hybrid",
        top_k: int = 10,
    ) -> dict[str, Any]:
        return self.multi_workspace.search(query, mode=mode, top_k=top_k)

    def capabilities(self) -> dict[str, Any]:
        caps = self.brain.capabilities()
        caps["multi_workspace"] = True
        caps["plugin_system"] = True
        caps["workspaces_loaded"] = self.multi_workspace.list_workspaces()
        return caps

    def upload_and_process(self, file_path: str | Path) -> dict[str, Any]:
        uploaded = self.sources.upload(Path(file_path))
        if "error" in uploaded:
            return uploaded
        inbox = Path(uploaded.get("absolute_path", uploaded["path"]))
        if not inbox.is_absolute():
            inbox = ROOT / inbox
        result = self.processing.process(inbox)
        self.sync_workspace_manifest()
        return result

    def knowledge_objects(self, limit: int = 10) -> list[dict[str, Any]]:
        return [self.knowledge_dna(d.doc_id) for d in self.brain.kb.documents[:limit]]
