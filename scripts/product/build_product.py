#!/usr/bin/env python3
"""Orchestrate full Zypher Product build pipeline."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

STEPS = [
    ("chunk_documents", "Build vector-ready chunks"),
    ("deduplicate", "Remove duplicate chunks"),
    ("validate_quality", "Validate quality gates"),
    ("export_graph", "Export graph relationships"),
    ("export_embeddings", "Generate embeddings"),
    ("build_benchmarks", "Build benchmark datasets"),
    ("build_manifest", "Build product manifest"),
    ("audit_distribution", "Audit distribution compliance"),
]


def run_step(script: str, config: Path, extra: list[str] | None = None) -> None:
    cmd = [sys.executable, str(Path(__file__).parent / f"{script}.py"), "--config", str(config)]
    if extra:
        cmd.extend(extra)
    print(f"\n=== {script} ===")
    subprocess.run(cmd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Zypher Product package")
    parser.add_argument("--config", type=Path, default=Path("config/product.yaml"))
    parser.add_argument("--skip-embeddings", action="store_true", help="Skip embedding generation")
    parser.add_argument("--skip-eval", action="store_true", help="Skip RAG evaluation")
    args = parser.parse_args()

    for script, _desc in STEPS:
        if args.skip_embeddings and script == "export_embeddings":
            continue
        run_step(script, args.config)

    if not args.skip_eval:
        run_step("evaluate_rag", args.config)

    print("\nProduct build complete.")


if __name__ == "__main__":
    main()
