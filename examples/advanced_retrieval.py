#!/usr/bin/env python3
"""Demonstrate Coltex advanced retrieval capabilities."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from brain.brain import Coltex


def main() -> None:
    # Lightweight config for demo — disable neural CE download in CI-like envs
    brain = Coltex(config_path=ROOT / "config" / "brain.yaml")
    # Prefer lexical CE fallback for fast demo unless model already cached
    brain.retrieval.cross_encoder.enabled = False

    print("=== Capabilities ===")
    print(json.dumps(brain.capabilities(), indent=2))

    # Ensure BM25/metadata/specialized are warm; vector may already be indexed
    counts = brain.index(force=False)
    print("\n=== Indexes ===")
    print(json.dumps(counts, indent=2))

    queries = [
        ("hybrid", "How does GraphRAG routing improve retrieval?"),
        ("bm25", "chunk overlap retrieval recall"),
        ("sql", "SELECT index schema migration"),
        ("code", "implement authentication service class"),
        ("api", "GET /v1/embeddings endpoint"),
        ("graphrag", "vector store dependency graph"),
        ("metadata", "runbook incident escalation"),
    ]

    for mode, query in queries:
        result = brain.retrieve(query, mode=mode, top_k=3)
        print(f"\n=== mode={mode} | {query} ===")
        print("sources:", (result.trace or {}).get("sources_used"))
        print("reranker:", (result.trace or {}).get("reranker"))
        for hit in result.documents:
            print(f"  - {hit.score:.3f} [{hit.source}] {hit.document.title[:80]}")


if __name__ == "__main__":
    main()
