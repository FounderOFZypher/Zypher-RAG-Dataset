"""Knowledge source upload and registration."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SUPPORTED = {".pdf", ".docx", ".md", ".markdown", ".txt", ".html", ".htm", ".json"}


class SourceManager:
    def __init__(
        self,
        inbox_dir: Path | str | None = None,
        processed_dir: Path | str | None = None,
        workspace=None,
    ):
        if workspace is not None:
            self.inbox = workspace.documents_inbox
            self.processed = workspace.knowledge
            self._root = workspace.root
        else:
            from runtime.runtime import ROOT

            self.inbox = Path(inbox_dir or ROOT / "data/sources/inbox")
            self.processed = Path(processed_dir or ROOT / "knowledge-base/uploads")
            self._root = ROOT
        self.inbox.mkdir(parents=True, exist_ok=True)
        self.processed.mkdir(parents=True, exist_ok=True)

    def list_sources(self) -> list[dict[str, Any]]:
        sources = []
        for directory in (self.inbox, self.processed):
            if not directory.exists():
                continue
            for path in sorted(directory.rglob("*")):
                if path.is_file() and path.suffix.lower() in SUPPORTED:
                    try:
                        rel = str(path.relative_to(self._root))
                    except ValueError:
                        rel = str(path)
                    sources.append({
                        "name": path.name,
                        "format": path.suffix.lstrip(".").lower(),
                        "path": rel,
                        "size_bytes": path.stat().st_size,
                        "status": "inbox" if "inbox" in path.parts else "processed",
                    })
        return sources

    def upload(self, source_path: Path) -> dict[str, Any]:
        source_path = Path(source_path)
        if not source_path.exists():
            return {"error": "file not found", "path": str(source_path)}
        if source_path.suffix.lower() not in SUPPORTED:
            return {"error": "unsupported format", "supported": sorted(SUPPORTED)}

        dest = self.inbox / source_path.name
        if source_path.resolve() != dest.resolve():
            shutil.copy2(source_path, dest)

        try:
            rel = str(dest.relative_to(self._root))
        except ValueError:
            rel = str(dest)

        return {
            "status": "uploaded",
            "name": dest.name,
            "format": dest.suffix.lstrip(".").lower(),
            "path": rel,
            "absolute_path": str(dest.resolve()),
            "uploaded_at": datetime.now(timezone.utc).isoformat(),
        }

    def count(self) -> int:
        return len(self.list_sources())
