#!/usr/bin/env python3
"""Evaluate RAG retrieval quality with evidence report."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from common import iter_jsonl, load_product_config, normalize_doc_id, resolve_path


def recall_at_k(retrieved_ids: list[str], relevant_ids: list[str], k: int) -> float:
    if not relevant_ids:
        return 0.0
    retrieved = {normalize_doc_id(i) for i in retrieved_ids[:k]}
    relevant = {normalize_doc_id(i) for i in relevant_ids}
    hits = retrieved & relevant
    return len(hits) / len(relevant)


def keyword_overlap(text: str, keywords: list[str]) -> float:
    if not keywords:
        return 0.0
    text_lower = text.lower()
    hits = sum(1 for kw in keywords if kw.lower() in text_lower)
    return hits / len(keywords)


def evaluate_retrieval(brain, gold_path: Path, top_k: int) -> dict:
    recalls: list[float] = []
    details: list[dict] = []

    for item in iter_jsonl(gold_path):
        query = item["query"]
        relevant = item["relevant_doc_ids"]
        result = brain.retrieve(query)
        retrieved_ids = [d.document.doc_id for d in result.documents]
        score = recall_at_k(retrieved_ids, relevant, top_k)
        recalls.append(score)
        details.append({
            "query": query,
            "recall_at_k": round(score, 4),
            "retrieved": retrieved_ids[:top_k],
            "relevant": relevant,
            "difficulty": item.get("difficulty", "unknown"),
        })

    avg = sum(recalls) / len(recalls) if recalls else 0.0
    return {
        "metric": f"recall@{top_k}",
        "value": round(avg, 4),
        "samples": len(recalls),
        "details": details,
    }


def evaluate_rag_faithfulness(brain, rag_path: Path, top_k: int) -> dict:
    scores: list[float] = []
    details: list[dict] = []

    for item in iter_jsonl(rag_path):
        query = item["question"]
        keywords = item.get("expected_keywords", [])
        result = brain.retrieve(query)
        context = result.context
        overlap = keyword_overlap(context, keywords)
        scores.append(overlap)
        details.append({
            "question": query,
            "keyword_overlap": round(overlap, 4),
            "expected_keywords": keywords,
            "context_chars": len(context),
        })

    avg = sum(scores) / len(scores) if scores else 0.0
    return {
        "metric": "context_keyword_overlap",
        "value": round(avg, 4),
        "samples": len(scores),
        "details": details,
    }


def evaluate_metadata_accuracy(kb) -> dict:
    correct = 0
    total = len(kb.documents)
    for doc in kb.documents:
        if doc.doc_id and doc.title:
            correct += 1
    accuracy = correct / total if total else 0.0
    return {
        "metric": "metadata_accuracy",
        "value": round(accuracy, 4),
        "samples": total,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate RAG pipeline quality")
    parser.add_argument("--config", type=Path, default=Path("config/product.yaml"))
    parser.add_argument("--brain-config", type=Path, default=Path("config/brain_curated.yaml"))
    args = parser.parse_args()

    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))

    from common import ensure_workspace_path, load_knowledge_base
    ensure_workspace_path()
    from brain.brain import ZypherBrain

    cfg = load_product_config(args.config)
    eval_cfg = cfg["evaluation"]
    bench_dir = resolve_path(cfg["benchmarks"]["output_dir"])
    top_k = int(eval_cfg.get("top_k", 8))

    brain_config = resolve_path(args.brain_config)
    brain = ZypherBrain(config_path=brain_config)
    brain.index(force=True)

    kb = load_knowledge_base(cfg)
    report: dict = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "brain_config": str(brain_config),
        "top_k": top_k,
        "metrics": {},
        "passed": True,
        "evidence": [],
    }

    gold_path = bench_dir / "retrieval_gold.jsonl"
    rag_path = bench_dir / "rag_eval.jsonl"

    if gold_path.exists():
        retrieval = evaluate_retrieval(brain, gold_path, top_k)
        report["metrics"]["retrieval"] = retrieval
        min_recall = float(eval_cfg.get("min_retrieval_recall", 0.5))
        passed = retrieval["value"] >= min_recall
        report["passed"] = report["passed"] and passed
        report["evidence"].append(
            f"Retrieval recall@{top_k}: {retrieval['value']:.2%} "
            f"(target ≥ {min_recall:.0%}, {'PASS' if passed else 'FAIL'})"
        )

    if rag_path.exists():
        faithfulness = evaluate_rag_faithfulness(brain, rag_path, top_k)
        report["metrics"]["faithfulness"] = faithfulness
        report["evidence"].append(
            f"Context keyword overlap: {faithfulness['value']:.2%} across {faithfulness['samples']} FAQ queries"
        )

    metadata = evaluate_metadata_accuracy(kb)
    report["metrics"]["metadata"] = metadata
    min_meta = float(eval_cfg.get("min_metadata_accuracy", 0.9))
    meta_passed = metadata["value"] >= min_meta
    report["passed"] = report["passed"] and meta_passed
    report["evidence"].append(
        f"Metadata accuracy: {metadata['value']:.2%} (target ≥ {min_meta:.0%}, {'PASS' if meta_passed else 'FAIL'})"
    )

    out_path = bench_dir / "evaluation_report.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(json.dumps({
        "passed": report["passed"],
        "report": str(out_path),
        "evidence": report["evidence"],
    }, indent=2))

    if not report["passed"]:
        raise SystemExit("Evaluation thresholds not met")


if __name__ == "__main__":
    main()
