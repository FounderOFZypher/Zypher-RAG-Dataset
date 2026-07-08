"""Active workspace session (.coltex-session)."""

from __future__ import annotations

import os
from pathlib import Path

SESSION_FILE = Path(".coltex-session")
ENV_VAR = "COLTEX_WORKSPACE"


def get_active_workspace() -> Path | None:
    env = os.environ.get(ENV_VAR)
    if env:
        path = Path(env).expanduser().resolve()
        if path.exists():
            return path
    if SESSION_FILE.exists():
        try:
            raw = SESSION_FILE.read_text(encoding="utf-8").strip()
            if raw:
                path = Path(raw).expanduser().resolve()
                if path.exists():
                    return path
        except OSError:
            pass
    return None


def set_active_workspace(manifest_path: Path) -> Path:
    manifest_path = manifest_path.resolve()
    SESSION_FILE.write_text(str(manifest_path) + "\n", encoding="utf-8")
    os.environ[ENV_VAR] = str(manifest_path)
    return manifest_path


def clear_active_workspace() -> None:
    os.environ.pop(ENV_VAR, None)
    if SESSION_FILE.exists():
        SESSION_FILE.unlink(missing_ok=True)
