"""V1 workspace settings."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


class SettingsStore:
    def __init__(
        self,
        path: str | Path | None = None,
        defaults_path: str | Path | None = None,
        workspace=None,
    ):
        if workspace is not None:
            self.path = workspace.settings_json_path
            self.defaults_path = Path(__file__).resolve().parent.parent.parent / "config/v1.yaml"
            self._workspace = workspace
        else:
            from runtime.runtime import ROOT

            self.path = Path(path or ROOT / "data/runtime/settings.json")
            self.defaults_path = Path(defaults_path or ROOT / "config/v1.yaml")
            self._workspace = None
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> dict[str, Any]:
        defaults = self._defaults()
        if self.path.exists():
            try:
                saved = json.loads(self.path.read_text(encoding="utf-8"))
                return {**defaults, **saved}
            except (json.JSONDecodeError, OSError):
                pass
        return defaults

    def save(self, updates: dict[str, Any]) -> dict[str, Any]:
        current = self.load()
        current.update(updates)
        self.path.write_text(json.dumps(current, indent=2), encoding="utf-8")
        if self._workspace is not None:
            self._workspace.write_brain_config(current)
        return current

    def _defaults(self) -> dict[str, Any]:
        if self.defaults_path.exists():
            cfg = yaml.safe_load(self.defaults_path.read_text(encoding="utf-8"))
            defaults = dict(cfg.get("settings", {}).get("defaults", {}))
            if self._workspace is not None:
                defaults["workspace"] = self._workspace.name
            return defaults
        base = {
            "workspace": self._workspace.name if self._workspace else "default",
            "ai_provider": "local",
            "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
            "chunk_size": 2000,
            "backup_enabled": False,
        }
        return base
