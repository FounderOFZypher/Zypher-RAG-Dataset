#!/usr/bin/env python3
"""Generate embeddings for vector-ready chunks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import iter_jsonl, load_product_config, resolve_path, write_jsonl


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate chunk embeddings")
    parser.add_argument("--config", type=Path, default=Path("config/product.yaml"))
    parser.add_argument("--batch-size", type=int, default=None)
    args = parser.parse_args()

    cfg = load_product_config(args.config)
    chunks_path = resolve_path(cfg["output"]["chunks"])
    if not chunks_path.exists():
        raise SystemExit(f"Chunks file not found: {chunks_path}. Run chunk_documents first.")

    emb_cfg = cfg["embeddings"]
    out_dir = resolve_path(emb_cfg["output_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "embeddings.jsonl"
    batch_size = args.batch_size or int(emb_cfg.get("batch_size", 64))

    from common import ensure_workspace_path
    ensure_workspace_path()
    from brain.embeddings.encoder import EmbeddingEncoder

    encoder = EmbeddingEncoder(emb_cfg["model"])
    chunks = list(iter_jsonl(chunks_path))
    records: list[dict] = []

    for start in range(0, len(chunks), batch_size):
        batch = chunks[start : start + batch_size]
        texts = [c["text"] for c in batch]
        vectors = encoder.encode(texts)
        for chunk, vector in zip(batch, vectors):
            records.append({
                "chunk_id": chunk["chunk_id"],
                "doc_id": chunk["doc_id"],
                "model": emb_cfg["model"],
                "dimensions": len(vector),
                "embedding": vector,
            })

    write_jsonl(out_path, records)

    manifest = {
        "model": emb_cfg["model"],
        "count": len(records),
        "dimensions": records[0]["dimensions"] if records else 0,
        "output": str(out_path),
    }
    with (out_dir / "manifest.json").open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
