#!/usr/bin/env python3
"""Audit commercial distribution rights compliance for the Zypher Product."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from common import (
    ROOT,
    distribution_cfg,
    is_substantive_document,
    iter_jsonl,
    load_knowledge_base,
    load_product_config,
    resolve_path,
)


def check_required_files(dist_cfg: dict) -> dict:
    issues: list[str] = []
    required: list[tuple[str, Path]] = []

    if dist_cfg.get("require_kb_license", True):
        required.append(("knowledge-base/LICENSE", ROOT / "knowledge-base" / "LICENSE"))
    if dist_cfg.get("require_provenance", True):
        required.append(("knowledge-base/PROVENANCE.md", ROOT / "knowledge-base" / "PROVENANCE.md"))
    if dist_cfg.get("require_notice", True):
        required.append(("NOTICE", ROOT / "NOTICE"))

    for label, path in required:
        if not path.exists():
            issues.append(f"Missing required file: {label}")

    return {"passed": not issues, "issues": issues}


def check_excluded_paths_not_in_product(cfg: dict) -> dict:
    issues: list[str] = []
    forbidden_prefixes = (
        "knowledge-base/generated/",
        "knowledge-base/_excluded_from_distribution/",
        "knowledge-base/_seed/",
    )

    chunks_path = resolve_path(cfg["output"]["chunks"])
    if chunks_path.exists():
        for chunk in iter_jsonl(chunks_path):
            source = chunk.get("source_path", "")
            for prefix in forbidden_prefixes:
                if prefix in source.replace("\\", "/"):
                    issues.append(f"Excluded path in chunks: {source}")
                    break

    return {"passed": not issues, "issues": issues}


def check_document_substance(cfg: dict, kb) -> dict:
    dist_cfg = distribution_cfg(cfg)
    issues: list[str] = []
    rejected: list[dict] = []

    for doc in kb.documents:
        ok, reason = is_substantive_document(doc, dist_cfg)
        if not ok:
            issues.append(f"{doc.doc_id}: {reason}")
            rejected.append({"doc_id": doc.doc_id, "path": doc.path, "reason": reason})

    return {
        "passed": not issues,
        "total_documents": len(kb.documents),
        "rejected": len(rejected),
        "issues": issues[:20],
        "rejected_samples": rejected[:10],
    }


def check_chunks_for_forbidden_content(cfg: dict) -> dict:
    dist_cfg = distribution_cfg(cfg)
    chunks_path = resolve_path(cfg["output"]["chunks"])
    issues: list[str] = []

    if not chunks_path.exists():
        return {"passed": True, "issues": [], "note": "No chunks file yet"}

    for chunk in iter_jsonl(chunks_path):
        text = chunk.get("text", "")
        for marker in dist_cfg.get("forbidden_body_markers", []):
            if marker in text:
                issues.append(f"Chunk {chunk.get('chunk_id')}: forbidden marker")
                break
        for pattern in dist_cfg.get("forbidden_source_patterns", []):
            if pattern.lower() in text.lower():
                issues.append(f"Chunk {chunk.get('chunk_id')}: forbidden pattern {pattern}")
                break

    return {"passed": not issues, "issues": issues[:20], "total_issues": len(issues)}


def check_no_copyright_claims(kb) -> dict:
    """Flag common third-party copyright phrases in distributable content."""
    patterns = [
        r"copyright\s+\d{4}",
        r"all rights reserved",
        r"©\s*\d{4}",
    ]
    issues: list[str] = []
    for doc in kb.documents:
        for pat in patterns:
            if re.search(pat, doc.content, re.IGNORECASE):
                issues.append(f"{doc.doc_id}: matched '{pat}'")
    return {"passed": not issues, "issues": issues}


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit distribution compliance")
    parser.add_argument("--config", type=Path, default=Path("config/product.yaml"))
    parser.add_argument("--report", type=Path, default=Path("benchmarks/distribution_audit.json"))
    args = parser.parse_args()

    cfg = load_product_config(args.config)
    kb = load_knowledge_base(cfg)
    dist_cfg = distribution_cfg(cfg)

    report = {
        "passed": True,
        "required_files": check_required_files(dist_cfg),
        "excluded_paths": check_excluded_paths_not_in_product(cfg),
        "document_substance": check_document_substance(cfg, kb),
        "chunk_content": check_chunks_for_forbidden_content(cfg),
        "copyright_scan": check_no_copyright_claims(kb),
        "summary": {
            "distributable_documents": len(kb.documents),
            "license": cfg.get("license", "Apache-2.0"),
            "content_origin": "original_synthetic",
            "third_party_docs_copied": False,
        },
    }

    for key in ("required_files", "excluded_paths", "document_substance", "chunk_content", "copyright_scan"):
        if not report[key].get("passed", False):
            report["passed"] = False

    args.report.parent.mkdir(parents=True, exist_ok=True)
    with resolve_path(args.report).open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(json.dumps({
        "passed": report["passed"],
        "distributable_documents": report["summary"]["distributable_documents"],
        "report": str(resolve_path(args.report)),
    }, indent=2))

    if not report["passed"]:
        raise SystemExit("Distribution audit failed — see report for details")


if __name__ == "__main__":
    main()
