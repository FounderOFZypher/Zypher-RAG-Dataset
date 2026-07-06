#!/usr/bin/env python3
"""Build curated benchmark datasets from seed knowledge base."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from common import (
    extract_faq_question,
    iter_jsonl,
    load_knowledge_base,
    load_product_config,
    normalize_doc_id,
    normalize_id_list,
    resolve_path,
    write_jsonl,
)


def _answer_keywords(doc) -> list[str]:
    """Extract key terms from document body for faithfulness checks."""
    text = doc.content.lower()
    words = re.findall(r"[a-z]{5,}", text)
    freq: dict[str, int] = {}
    for w in words:
        if w in ("zypher", "retrieval", "graphrag", "chunking", "embedding", "vector", "knowledge"):
            freq[w] = freq.get(w, 0) + 3
        else:
            freq[w] = freq.get(w, 0) + 1
    return [w for w, _ in sorted(freq.items(), key=lambda x: -x[1])[:8]]


def build_faq_benchmark(kb, min_pairs: int) -> list[dict]:
    pairs: list[dict] = []
    seen_ids: set[str] = set()

    for doc in kb.documents:
        question = extract_faq_question(doc)
        if not question or doc.doc_id in seen_ids:
            continue
        seen_ids.add(doc.doc_id)
        pairs.append({
            "id": f"faq-{normalize_doc_id(doc.doc_id)}",
            "question": question,
            "expected_doc_ids": [normalize_doc_id(doc.doc_id)],
            "expected_keywords": _answer_keywords(doc),
            "category": doc.category,
            "tags": doc.tags,
            "source_path": doc.path,
        })

    # Supplement with title-based queries from diverse, well-connected documents
    if len(pairs) < min_pairs:
        candidates = sorted(
            kb.documents,
            key=lambda d: (len(d.related), len(d.content)),
            reverse=True,
        )
        for doc in candidates:
            if doc.doc_id in seen_ids:
                continue
            title = doc.title.strip()
            if len(title) < 15 or title.lower().startswith("chunk "):
                continue
            question = title if title.endswith("?") else f"What does Zypher document about {title}?"
            seen_ids.add(doc.doc_id)
            pairs.append({
                "id": f"faq-{doc.doc_id}",
                "question": question,
                "expected_doc_ids": [doc.doc_id],
                "expected_keywords": _answer_keywords(doc),
                "category": doc.category,
                "tags": doc.tags,
                "source_path": doc.path,
                "supplemental": True,
            })
            if len(pairs) >= min_pairs:
                break

    if len(pairs) < min_pairs:
        raise SystemExit(f"Only {len(pairs)} benchmark pairs found; need {min_pairs}")
    return pairs


def build_faq_from_catalog(catalog_path: Path, min_pairs: int, sample_size: int) -> list[dict]:
    pairs: list[dict] = []
    seen: set[str] = set()
    for i, rec in enumerate(iter_jsonl(catalog_path)):
        if sample_size and i >= sample_size:
            break
        doc_id = rec.get("doc_id", "")
        if doc_id in seen:
            continue
        title = str(rec.get("title", "")).strip()
        doc_type = rec.get("doc_type", "")
        if doc_type == "faq" or "?" in title:
            question = title.split("—")[0].strip() if "—" in title else title
        else:
            question = f"What are the best practices for {title.split('—')[0].strip()}?"
        tags = rec.get("tags", [])
        pairs.append({
            "id": f"faq-{doc_id}",
            "question": question,
            "expected_doc_ids": [doc_id],
            "expected_keywords": [t for t in tags[:8] if isinstance(t, str)],
            "category": rec.get("category", ""),
            "tags": tags,
            "source_path": rec.get("path", ""),
            "from_catalog": True,
        })
        seen.add(doc_id)
        if len(pairs) >= min_pairs:
            break
    if len(pairs) < min_pairs:
        raise SystemExit(f"Only {len(pairs)} catalog benchmark pairs; need {min_pairs}")
    return pairs


def build_retrieval_gold_catalog(faq_pairs: list[dict]) -> list[dict]:
    gold: list[dict] = []
    for pair in faq_pairs:
        gold.append({
            "query": pair["question"],
            "relevant_doc_ids": pair["expected_doc_ids"],
            "relevant_chunk_ids": [],
            "difficulty": "medium",
        })
    return gold


def build_retrieval_gold(faq_pairs: list[dict], kb) -> list[dict]:
    gold: list[dict] = []
    for pair in faq_pairs:
        gold.append({
            "query": pair["question"],
            "relevant_doc_ids": pair["expected_doc_ids"],
            "relevant_chunk_ids": [],
            "difficulty": "easy",
        })

    hub_docs = sorted(kb.documents, key=lambda d: len(d.related), reverse=True)[:5]
    for doc in hub_docs:
        if len(doc.related) < 3:
            continue
        gold.append({
            "query": f"What documents are related to {doc.title}?",
            "relevant_doc_ids": normalize_id_list([doc.doc_id] + doc.related[:8]),
            "relevant_chunk_ids": [],
            "difficulty": "hard",
        })
    return gold


def build_rag_eval(faq_pairs: list[dict]) -> list[dict]:
    eval_set: list[dict] = []
    for pair in faq_pairs:
        eval_set.append({
            "id": pair["id"],
            "question": pair["question"],
            "expected_doc_ids": pair["expected_doc_ids"],
            "expected_keywords": pair["expected_keywords"],
            "rubric": "Answer must cite facts from expected documents only.",
        })
    return eval_set


def main() -> None:
    parser = argparse.ArgumentParser(description="Build benchmark datasets")
    parser.add_argument("--config", type=Path, default=Path("config/product.yaml"))
    args = parser.parse_args()

    cfg = load_product_config(args.config)
    bench_cfg = cfg["benchmarks"]
    out_dir = resolve_path(bench_cfg["output_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)

    kb = load_knowledge_base(cfg)
    min_faq = int(bench_cfg.get("min_faq_pairs", 10))
    catalog_path = resolve_path(cfg["output"].get("catalog", "data/product/catalog.jsonl"))

    if bench_cfg.get("sample_from_catalog") and catalog_path.exists():
        sample = int(bench_cfg["sample_from_catalog"])
        faq_pairs = build_faq_from_catalog(catalog_path, min_faq, sample)
        gold_builder = lambda: build_retrieval_gold_catalog(faq_pairs)
    else:
        faq_pairs = build_faq_benchmark(kb, min_faq)
        gold_builder = lambda: build_retrieval_gold(faq_pairs, kb)

    write_jsonl(out_dir / "faq_pairs.jsonl", faq_pairs)

    gold: list[dict] = []
    rag_eval: list[dict] = []

    if bench_cfg.get("include_retrieval_gold", True):
        gold = gold_builder()
        write_jsonl(out_dir / "retrieval_gold.jsonl", gold)

    if bench_cfg.get("include_rag_eval", True):
        rag_eval = build_rag_eval(faq_pairs)
        write_jsonl(out_dir / "rag_eval.jsonl", rag_eval)

    summary = {
        "faq_pairs": len(faq_pairs),
        "retrieval_gold": len(gold) if bench_cfg.get("include_retrieval_gold", True) else 0,
        "rag_eval": len(rag_eval) if bench_cfg.get("include_rag_eval", True) else 0,
        "output_dir": str(out_dir),
    }
    with (out_dir / "benchmark_manifest.json").open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
