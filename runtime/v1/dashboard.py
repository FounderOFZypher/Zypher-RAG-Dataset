"""Coltex V1 dashboard — honest metrics."""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class V1Dashboard:
    def __init__(self, runtime):
        self._rt = runtime

    def snapshot(self) -> dict[str, Any]:
        health = self._rt.analytics.health()
        brain = self._rt.brain.stats()
        usage = self._rt.ask.usage_stats()
        sources = self._rt.sources.count()
        graph = self._rt.graph.stats()

        dup_count = self._count_duplicate_groups()
        outdated = self._count_outdated()
        last_sync = self._last_sync_time()
        ws = self._rt.workspace

        payload = {
            "product": "Coltex V1",
            "tagline": "The AI Knowledge Platform for Modern Organizations",
            "dashboard": {
                "documents": brain.get("documents", 0),
                "sources": sources,
                "searches": usage.get("searches", 0),
                "ai_queries": usage.get("ask", 0),
                "last_sync": last_sync,
                "health": {
                    "knowledge_score": health.get("knowledge_score", 0),
                    "documents": brain.get("documents", 0),
                    "embeddings": brain.get("indexed_vectors", 0),
                    "graph_nodes": graph.get("graph_edges", 0) + brain.get("documents", 0),
                    "duplicates": dup_count,
                    "outdated": outdated,
                },
            },
        }
        if ws is not None:
            payload["workspace"] = {
                "name": ws.name,
                "manifest": str(ws.manifest_path),
                "size_bytes": ws.dir_size_bytes(),
            }
        return payload

    def _count_duplicate_groups(self) -> int:
        from collections import Counter

        titles = [d.title.strip().lower() for d in self._rt.brain.kb.documents if d.title]
        if not titles:
            return 0
        counts = Counter(titles)
        return sum(1 for c in counts.values() if c > 1)

    def _count_outdated(self) -> int:
        count = 0
        for doc in self._rt.brain.kb.documents:
            if "deprecated" in (doc.content or "")[:500].lower():
                count += 1
            elif len(doc.content or "") < 80:
                count += 1
        return min(count, 999)

    def _last_sync_time(self) -> str | None:
        log = self._rt.data_dir / "events.jsonl"
        if log.exists():
            try:
                ts = datetime.fromtimestamp(log.stat().st_mtime, tz=timezone.utc)
                return ts.isoformat()
            except OSError:
                pass
        return None
