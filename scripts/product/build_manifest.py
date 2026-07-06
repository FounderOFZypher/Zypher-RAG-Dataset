#!/usr/bin/env python3
"""Build product manifest with checksums and metadata."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from common import iter_jsonl, load_knowledge_base, load_product_config, resolve_path


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def count_jsonl(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for _ in iter_jsonl(path))


def main() -> None:
    parser = argparse.ArgumentParser(description="Build product manifest")
    parser.add_argument("--config", type=Path, default=Path("config/product.yaml"))
    args = parser.parse_args()

    cfg = load_product_config(args.config)
    kb = load_knowledge_base(cfg)
    out_cfg = cfg["output"]
    base_dir = resolve_path(out_cfg["base_dir"])

    artifacts = {
        "chunks": resolve_path(out_cfg["chunks"]),
        "graph": resolve_path(out_cfg["graph"]),
        "metadata": resolve_path(out_cfg["metadata"]),
        "embeddings": resolve_path(cfg["embeddings"]["output_dir"]) / "embeddings.jsonl",
    }

    files: dict[str, dict] = {}
    for name, path in artifacts.items():
        if path.exists():
            files[name] = {
                "path": str(path.relative_to(resolve_path("."))),
                "sha256": file_sha256(path),
                "records": count_jsonl(path) if path.suffix == ".jsonl" else None,
                "bytes": path.stat().st_size,
            }

    # Export document metadata index
    meta_path = resolve_path(out_cfg["metadata"])
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    documents = []
    for doc in kb.documents:
        documents.append({
            "doc_id": doc.doc_id,
            "title": doc.title,
            "category": doc.category,
            "doc_type": doc.doc_type,
            "tags": doc.tags,
            "hub": doc.hub,
            "related_count": len(doc.related),
            "relationship_types": list(doc.relationships.keys()),
            "source_path": doc.path,
            "license": cfg.get("license", "Apache-2.0"),
        })
    with meta_path.open("w", encoding="utf-8") as f:
        json.dump({"documents": documents, "count": len(documents)}, f, indent=2)

    files["metadata"] = {
        "path": str(meta_path.relative_to(resolve_path("."))),
        "sha256": file_sha256(meta_path),
        "records": len(documents),
        "bytes": meta_path.stat().st_size,
    }

    manifest = {
        "name": cfg.get("name", "Zypher Brain Product"),
        "version": str(cfg.get("version", "1.0.0")),
        "license": cfg.get("license", "Apache-2.0"),
        "updated": str(cfg.get("updated", datetime.now(timezone.utc).strftime("%Y-%m-%d"))),
        "built_at": datetime.now(timezone.utc).isoformat(),
        "curated_only": cfg["quality"].get("curated_only", True),
        "documents": len(kb.documents),
        "artifacts": files,
        "benchmarks_dir": cfg["benchmarks"]["output_dir"],
    }

    manifest_path = resolve_path(out_cfg["manifest"])
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
