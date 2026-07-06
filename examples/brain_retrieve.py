#!/usr/bin/env python3
"""Example: retrieve from product chunks without full brain stack."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from brain.embeddings.encoder import EmbeddingEncoder


def load_chunks(path: Path) -> list[dict]:
    chunks = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                chunks.append(json.loads(line))
    return chunks


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x * x for x in a) ** 0.5
    norm_b = sum(x * x for x in b) ** 0.5
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0


def main() -> None:
    query = sys.argv[1] if len(sys.argv) > 1 else "How does GraphRAG work?"
    chunks_path = Path("data/product/chunks/chunks.jsonl")
    emb_path = Path("data/product/embeddings/embeddings.jsonl")

    if not chunks_path.exists():
        print("Run `make product` first to build chunks and embeddings.")
        sys.exit(1)

    chunks = load_chunks(chunks_path)
    chunk_by_id = {c["chunk_id"]: c for c in chunks}

    if emb_path.exists():
        embeddings = {}
        with emb_path.open(encoding="utf-8") as f:
            for line in f:
                rec = json.loads(line)
                embeddings[rec["chunk_id"]] = rec["embedding"]
        encoder = EmbeddingEncoder()
        query_vec = encoder.encode_query(query)
        scored = []
        for cid, vec in embeddings.items():
            chunk = chunk_by_id.get(cid)
            if chunk:
                scored.append((cosine_similarity(query_vec, vec), chunk))
        scored.sort(key=lambda x: -x[0])
    else:
        query_lower = query.lower()
        scored = []
        for chunk in chunks:
            score = sum(1 for w in query_lower.split() if w in chunk["text"].lower())
            scored.append((score, chunk))
        scored.sort(key=lambda x: -x[0])

    print(f"Query: {query}\n")
    for score, chunk in scored[:5]:
        print(f"  [{score:.3f}] {chunk['title']} — {chunk['text'][:120]}...")


if __name__ == "__main__":
    main()
