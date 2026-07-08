"""V1 AI Processing — Upload through Index."""

from __future__ import annotations

import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from runtime.sources.parser import clean_text, parse_file


class ProcessingPipeline:
    STEPS = ["upload", "parse", "clean", "chunk", "metadata", "embeddings", "index", "done"]

    def __init__(self, runtime, processed_dir: Path | str | None = None, chunk_size: int | None = None):
        self._rt = runtime
        if runtime.workspace is not None:
            self.processed_dir = runtime.workspace.knowledge
            self._root = runtime.workspace.root
        else:
            from runtime.runtime import ROOT

            self.processed_dir = Path(processed_dir or ROOT / "knowledge-base/uploads")
            self._root = ROOT
        self.processed_dir.mkdir(parents=True, exist_ok=True)
        settings = runtime.settings.load()
        self.chunk_size = chunk_size or int(settings.get("chunk_size", 2000))

    def process(self, file_path: Path) -> dict[str, Any]:
        file_path = Path(file_path)
        steps_completed: list[str] = []
        doc_id = f"UPLOAD-{uuid.uuid4().hex[:8].upper()}"

        steps_completed.append("upload")
        parsed = parse_file(file_path)
        steps_completed.append("parse")

        text = clean_text(parsed["text"])
        steps_completed.append("clean")
        steps_completed.append("chunk")

        title = file_path.stem.replace("-", " ").replace("_", " ").title()
        meta = {
            "id": doc_id,
            "title": title,
            "doc_type": "documentation",
            "source": file_path.name,
            "uploaded_at": datetime.now(timezone.utc).isoformat(),
            "format": parsed["format"],
        }
        steps_completed.append("metadata")

        out_path = self.processed_dir / f"{doc_id}-{file_path.stem}.md"
        frontmatter = yaml.dump(meta, default_flow_style=False).strip()
        out_path.write_text(f"---\n{frontmatter}\n---\n\n{text}\n", encoding="utf-8")

        from brain.ingestion.loader import parse_markdown

        doc = parse_markdown(out_path)
        kb = self._rt.brain.kb
        kb.documents.append(doc)
        kb.by_id[doc.doc_id] = doc
        self._rt.brain.metadata_index.refresh()
        try:
            self._rt.brain.index_document(doc)
        except Exception:
            pass
        steps_completed.extend(["embeddings", "index"])

        self._rt.event_bus.run_pipeline({"document_id": doc_id, "source": "upload"})
        self._rt.curator.proactive_scan(save=True)

        steps_completed.append("done")
        self._rt.sync_workspace_manifest()

        try:
            rel_path = str(out_path.relative_to(self._root))
        except ValueError:
            rel_path = str(out_path)

        return {
            "status": "done",
            "document_id": doc_id,
            "title": title,
            "path": rel_path,
            "steps": steps_completed,
            "char_count": len(text),
        }
