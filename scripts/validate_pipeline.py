#!/usr/bin/env python3
"""Validate repo setup, data files, and training checkpoints."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def check(name: str, ok: bool, detail: str = "") -> bool:
    status = "OK" if ok else "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f" — {detail}"
    print(line)
    return ok


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Zypher training pipeline")
    parser.add_argument("--require-checkpoint", choices=["pretrain", "sft", "none"], default="none")
    parser.add_argument("--require-tokenizer", action="store_true")
    args = parser.parse_args()

    root = Path(".")
    all_ok = True

    # Python deps
    for pkg in ("torch", "yaml", "tokenizers"):
        try:
            __import__(pkg if pkg != "yaml" else "yaml")
            check(f"import {pkg}", True)
        except ImportError:
            all_ok = check(f"import {pkg}", False, "run: pip install -r requirements.txt")

    # Config files
    for path in (
        "config/chatbot.yaml",
        "config/training.yaml",
        "config/corpus_generation.yaml",
        "requirements.txt",
    ):
        all_ok = check(f"file {path}", (root / path).exists()) and all_ok

    # Data files
    data_files = {
        "data/advanced/train.jsonl": "Run: make prepare-advanced",
        "data/advanced/val.jsonl": "Run: make prepare-advanced",
        "data/advanced/pretrain.txt": "Run: make prepare-advanced",
    }
    for path, hint in data_files.items():
        p = root / path
        ok = p.exists() and p.stat().st_size > 0
        all_ok = check(f"data {path}", ok, hint if not ok else f"{p.stat().st_size:,} bytes") and all_ok

    stats_path = root / "data/advanced/dataset_stats.json"
    if stats_path.exists():
        stats = json.loads(stats_path.read_text(encoding="utf-8"))
        all_ok = check("training examples", stats.get("total_examples", 0) > 0, str(stats.get("total_examples"))) and all_ok

    # Tokenizer
    tok_path = root / "outputs/tokenizer/tokenizer.json"
    tok_ok = tok_path.exists()
    if args.require_tokenizer:
        all_ok = check("tokenizer", tok_ok, "Run: make train-tokenizer") and all_ok
    else:
        check("tokenizer", tok_ok, "Run: make train-tokenizer" if not tok_ok else str(tok_path))

    # Checkpoints
    pretrain_ckpt = root / "outputs/pretrain/checkpoint-final/model.pt"
    sft_ckpt = root / "outputs/sft/checkpoint-final/model.pt"

    if args.require_checkpoint in ("pretrain", "sft"):
        all_ok = check("pretrain checkpoint", pretrain_ckpt.exists(), str(pretrain_ckpt)) and all_ok
    else:
        check("pretrain checkpoint", pretrain_ckpt.exists(), "optional until after pretrain")

    if args.require_checkpoint == "sft":
        all_ok = check("sft checkpoint", sft_ckpt.exists(), str(sft_ckpt)) and all_ok
    else:
        check("sft checkpoint", sft_ckpt.exists(), "optional until after sft")

    # Knowledge base
    kb_count = len(list((root / "knowledge-base").rglob("CHUNK-*.md"))) if (root / "knowledge-base").exists() else 0
    all_ok = check("seed knowledge-base chunks", kb_count > 0, f"{kb_count} files") and all_ok

    if not all_ok:
        print("\nValidation failed. Fix the items above before training.")
        sys.exit(1)

    print("\nValidation passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
