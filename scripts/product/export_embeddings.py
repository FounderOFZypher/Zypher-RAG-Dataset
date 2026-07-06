#!/usr/bin/env python3
"""Generate embeddings for vector-ready chunks (streaming-safe)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import iter_jsonl, load_product_config, resolve_path


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
    max_chunks = int(emb_cfg.get("max_chunks", 0))

    from common import ensure_workspace_path
    ensure_workspace_path()
    from brain.embeddings.encoder import EmbeddingEncoder

    encoder = EmbeddingEncoder(emb_cfg["model"])
    total = 0
    dimensions = 0

    with out_path.open("w", encoding="utf-8") as out_f:
        batch: list[dict] = []
        for chunk in iter_jsonl(chunks_path):
            if max_chunks and total >= max_chunks:
                break
            batch.append(chunk)
            if len(batch) >= batch_size:
                texts = [c["text"] for c in batch]
                vectors = encoder.encode(texts)
                for c, vector in zip(batch, vectors):
                    dimensions = len(vector)
                    out_f.write(json.dumps({
                        "chunk_id": c["chunk_id"],
                        "doc_id": c["doc_id"],
                        "model": emb_cfg["model"],
                        "dimensions": dimensions,
                        "embedding": vector,
                    }, ensure_ascii=False) + "\n")
                    total += 1
                batch = []
        if batch and (not max_chunks or total < max_chunks):
            remaining = batch[: max(0, max_chunks - total)] if max_chunks else batch
            vectors = encoder.encode([c["text"] for c in remaining])
            for c, vector in zip(remaining, vectors):
                dimensions = len(vector)
                out_f.write(json.dumps({
                    "chunk_id": c["chunk_id"],
                    "doc_id": c["doc_id"],
                    "model": emb_cfg["model"],
                    "dimensions": dimensions,
                    "embedding": vector,
                }, ensure_ascii=False) + "\n")
                total += 1

    manifest = {
        "model": emb_cfg["model"],
        "count": total,
        "dimensions": dimensions,
        "max_chunks_cap": max_chunks or None,
        "output": str(out_path),
    }
    with (out_dir / "manifest.json").open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
