#!/usr/bin/env python3
"""Remove duplicate chunks by content hash."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import iter_jsonl, load_product_config, resolve_path, write_jsonl


def deduplicate_chunks(chunks_path: Path) -> tuple[list[dict], int]:
    unique: list[dict] = []
    seen_hashes: set[str] = set()
    removed = 0

    for chunk in iter_jsonl(chunks_path):
        content_hash = chunk.get("content_hash", "")
        if content_hash and content_hash in seen_hashes:
            removed += 1
            continue
        if content_hash:
            seen_hashes.add(content_hash)
        unique.append(chunk)
    return unique, removed


def main() -> None:
    parser = argparse.ArgumentParser(description="Deduplicate product chunks")
    parser.add_argument("--config", type=Path, default=Path("config/product.yaml"))
    args = parser.parse_args()

    cfg = load_product_config(args.config)
    chunks_path = resolve_path(cfg["output"]["chunks"])
    if not chunks_path.exists():
        raise SystemExit(f"Chunks file not found: {chunks_path}. Run chunk_documents first.")

    unique, removed = deduplicate_chunks(chunks_path)
    write_jsonl(chunks_path, unique)

    total = len(unique) + removed
    ratio = removed / total if total else 0.0
    max_ratio = float(cfg["quality"]["max_duplicate_ratio"])

    result = {
        "before": total,
        "after": len(unique),
        "removed": removed,
        "duplicate_ratio": round(ratio, 4),
        "max_allowed_ratio": max_ratio,
        "passed": ratio <= max_ratio,
    }
    print(json.dumps(result, indent=2))

    if ratio > max_ratio:
        raise SystemExit(f"Duplicate ratio {ratio:.2%} exceeds max {max_ratio:.2%}")


if __name__ == "__main__":
    main()
