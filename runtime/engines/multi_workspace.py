"""Multi-workspace federated retrieval."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from brain.brain import Coltex
from brain.reranking.reranker import Reranker
from brain.types import RetrievalResult, ScoredDocument
from runtime.workspace.context import WorkspaceContext
from runtime.workspace.manifest import load_manifest


class MultiWorkspaceSearch:
    """
    Federated search across multiple `.ctex` workspaces.

    Each workspace keeps an isolated vector store and knowledge root.
    Results are fused with reciprocal-style weighted merge and tagged
    with the originating workspace name.
    """

    def __init__(self, workspace_roots: list[Path] | None = None):
        self.workspace_roots = [Path(p) for p in (workspace_roots or [])]
        self._engines: dict[str, Coltex] = {}

    def add_workspace(self, manifest_or_root: str | Path) -> str:
        path = Path(manifest_or_root).expanduser().resolve()
        if path.is_dir():
            matches = list(path.glob("*.ctex"))
            if not matches:
                raise FileNotFoundError(f"No .ctex manifest in {path}")
            path = matches[0]
        ctx = WorkspaceContext.from_manifest(path)
        ctx.ensure_layout()
        brain = Coltex(config=ctx.load_brain_config())
        name = ctx.name
        self._engines[name] = brain
        self.workspace_roots.append(ctx.root)
        return name

    def list_workspaces(self) -> list[str]:
        return sorted(self._engines.keys())

    def search(
        self,
        query: str,
        mode: str | None = "hybrid",
        top_k: int = 10,
        per_workspace_k: int = 8,
    ) -> dict[str, Any]:
        if not self._engines:
            return {"query": query, "workspaces": [], "results": [], "error": "no workspaces loaded"}

        fused: list[ScoredDocument] = []
        per_ws: dict[str, list[dict[str, Any]]] = {}
        for name, brain in self._engines.items():
            try:
                result = brain.retrieve(query, mode=mode, top_k=per_workspace_k)
            except Exception as exc:
                per_ws[name] = [{"error": str(exc)}]
                continue
            tagged: list[ScoredDocument] = []
            rows = []
            for scored in result.documents:
                tagged.append(ScoredDocument(
                    document=scored.document,
                    score=scored.score,
                    source=f"{scored.source}+workspace:{name}",
                ))
                rows.append({
                    "id": scored.document.doc_id,
                    "title": scored.document.title,
                    "score": round(scored.score, 4),
                    "source": scored.source,
                    "workspace": name,
                })
            per_ws[name] = rows
            fused.extend(tagged)

        merged = Reranker().merge(fused, top_k=top_k)
        return {
            "query": query,
            "mode": mode,
            "workspaces": self.list_workspaces(),
            "per_workspace": per_ws,
            "results": [
                {
                    "id": s.document.doc_id,
                    "title": s.document.title,
                    "score": round(s.score, 4),
                    "source": s.source,
                    "path": s.document.path,
                }
                for s in merged
            ],
        }
