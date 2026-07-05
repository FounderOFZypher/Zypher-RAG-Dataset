#!/usr/bin/env python3
"""Build advanced multi-task training data from the full knowledge corpus."""

from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path
from typing import Any

import yaml

SYSTEM_PROMPT = (
    "You are a custom AI assistant built from scratch. You specialize in software engineering, "
    "RAG/GraphRAG systems, debugging, architecture, security, and production operations. "
    "Think step by step, cite trade-offs, and provide actionable guidance."
)

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
ANSWER_RE = re.compile(r"\*\*Answer:\*\*\s*(.+)", re.DOTALL | re.IGNORECASE)


def parse_markdown(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    metadata: dict[str, Any] = {}
    body = text

    match = FRONTMATTER_RE.match(text)
    if match:
        try:
            loaded = yaml.safe_load(match.group(1))
            metadata = loaded if isinstance(loaded, dict) else {}
        except yaml.YAMLError:
            metadata = {}
        body = text[match.end() :].strip()

    # Legacy double-frontmatter chunks
    if not metadata and text.count("---") >= 2:
        parts = text.split("---")
        if len(parts) >= 3:
            try:
                loaded = yaml.safe_load(parts[1].strip())
                metadata = loaded if isinstance(loaded, dict) else {}
            except yaml.YAMLError:
                metadata = {}
            body = "---".join(parts[2:]).strip()

    return metadata, body


def extract_title(metadata: dict[str, Any], body: str) -> str:
    title = metadata.get("title")
    if isinstance(title, str) and title.strip():
        return title.strip()
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path_stem_title(metadata)


def path_stem_title(metadata: dict[str, Any]) -> str:
    slug = metadata.get("topic_slug") or metadata.get("id") or "topic"
    return str(slug).replace("_", " ").title()


def section_text(body: str) -> str:
    lines = body.splitlines()
    if lines and lines[0].startswith("#"):
        lines = lines[1:]
    return "\n".join(lines).strip()


def example(messages: list[dict[str, str]], **meta: Any) -> dict[str, Any]:
    return {"messages": messages, "metadata": meta}


def single_turn_qa(metadata: dict, body: str, source: str) -> list[dict[str, Any]]:
    title = extract_title(metadata, body)
    content = section_text(body)
    if len(content) < 60:
        return []

    results = []
    answer_match = ANSWER_RE.search(body)
    if answer_match:
        question = title if title.endswith("?") else f"What is {title}?"
        results.append(
            example(
                [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": question},
                    {"role": "assistant", "content": answer_match.group(1).strip()},
                ],
                task_type="faq",
                source=source,
                difficulty=metadata.get("difficulty", "intermediate"),
            )
        )

    tags = metadata.get("tags") or []
    tag_hint = f" Tags: {', '.join(tags)}." if tags else ""
    results.append(
        example(
            [
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"Explain in depth: {title}.{tag_hint}",
                },
                {"role": "assistant", "content": content},
            ],
            task_type="documentation",
            source=source,
            difficulty=metadata.get("difficulty", "intermediate"),
        )
    )
    return results


def multi_turn_dialogue(metadata: dict, body: str, source: str) -> list[dict[str, Any]]:
    title = extract_title(metadata, body)
    content = section_text(body)
    if len(content) < 120:
        return []

    category = metadata.get("category", "general")
    return [
        example(
            [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"I'm working on {category}. Where should I start with {title}?"},
                {
                    "role": "assistant",
                    "content": f"Start by clarifying constraints and success metrics for {title}. "
                    f"I'll outline a practical path.\n\n{content[:800]}",
                },
                {"role": "user", "content": "What are the top risks and how do we mitigate them?"},
                {
                    "role": "assistant",
                    "content": "Top risks: (1) silent data quality regressions, (2) latency spikes under load, "
                    "(3) security gaps in tool execution. Mitigate with validation gates, SLO dashboards, "
                    "and least-privilege tool policies. " + content[-400:],
                },
            ],
            task_type="multi_turn_dialogue",
            source=source,
            difficulty=metadata.get("difficulty", "intermediate"),
        )
    ]


def chain_of_thought(metadata: dict, body: str, source: str) -> list[dict[str, Any]]:
    title = extract_title(metadata, body)
    content = section_text(body)
    if len(content) < 100:
        return []

    return [
        example(
            [
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"Analyze trade-offs for {title}. Show your reasoning.",
                },
                {
                    "role": "assistant",
                    "content": (
                        "<|think|>\n"
                        "1. Identify requirements and constraints.\n"
                        "2. Compare approaches on latency, cost, and operability.\n"
                        "3. Choose a recommendation with rollback plan.\n"
                        "<|/think|>\n\n"
                        f"**Recommendation for {title}:**\n\n{content}"
                    ),
                },
            ],
            task_type="chain_of_thought",
            source=source,
            difficulty=metadata.get("difficulty", "intermediate"),
        )
    ]


def tool_calling(metadata: dict, body: str, source: str) -> list[dict[str, Any]]:
    title = extract_title(metadata, body)
    category = metadata.get("category", "system")
    content = section_text(body)
    if len(content) < 80:
        return []

    return [
        example(
            [
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"Investigate production metrics for {title} and summarize findings.",
                },
                {
                    "role": "assistant",
                    "content": (
                        '<|tool|>{"name": "query_metrics", "arguments": {"service": "'
                        + category
                        + '", "window": "1h"}}<|tool|>\n'
                        '<|tool_result|>{"p95_ms": 842, "error_rate": 0.012, "cpu": 0.78}<|tool_result|>\n\n'
                        f"Metrics show elevated p95 latency. Based on {title}:\n\n{content[:600]}"
                    ),
                },
            ],
            task_type="tool_calling",
            source=source,
            difficulty=metadata.get("difficulty", "intermediate"),
        )
    ]


def rag_with_context(metadata: dict, body: str, source: str) -> list[dict[str, Any]]:
    title = extract_title(metadata, body)
    content = section_text(body)
    if len(content) < 100:
        return []

    context = content[: min(1200, len(content))]
    return [
        example(
            [
                {"role": "system", "content": SYSTEM_PROMPT + " Use the provided context when answering."},
                {
                    "role": "user",
                    "content": f"<context>\n{context}\n</context>\n\nBased on the context, answer: {title}",
                },
                {"role": "assistant", "content": content},
            ],
            task_type="rag_with_context",
            source=source,
            difficulty=metadata.get("difficulty", "intermediate"),
        )
    ]


def code_tasks(metadata: dict, body: str, source: str) -> list[dict[str, Any]]:
    if "```" not in body:
        return []

    title = extract_title(metadata, body)
    blocks = re.findall(r"```[\w]*\n(.*?)```", body, re.DOTALL)
    if not blocks:
        return []

    code = blocks[0].strip()
    doc_type = metadata.get("doc_type", "")
    results = []

    if doc_type in ("code_walkthrough", "tutorial", "guide"):
        results.append(
            example(
                [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": f"Write production-ready code for: {title}",
                    },
                    {"role": "assistant", "content": f"```python\n{code}\n```\n\n{section_text(body)[:400]}"},
                ],
                task_type="code_generation",
                source=source,
                difficulty=metadata.get("difficulty", "intermediate"),
            )
        )

    results.append(
        example(
            [
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"Review this code from `{title}` and suggest improvements:\n\n```\n{code}\n```",
                },
                {
                    "role": "assistant",
                    "content": (
                        "Findings:\n"
                        "1. Add input validation and explicit error types.\n"
                        "2. Extract magic numbers to named constants.\n"
                        "3. Add structured logging and tracing hooks.\n"
                        "4. Include unit tests for edge cases.\n\n"
                        + section_text(body)[:500]
                    ),
                },
            ],
            task_type="code_review",
            source=source,
            difficulty=metadata.get("difficulty", "intermediate"),
        )
    )
    return results


GENERATORS = [
    single_turn_qa,
    multi_turn_dialogue,
    chain_of_thought,
    tool_calling,
    rag_with_context,
    code_tasks,
]


def collect_examples(kb_dirs: list[Path]) -> list[dict[str, Any]]:
    examples: list[dict[str, Any]] = []
    paths: list[Path] = []
    for kb_dir in kb_dirs:
        paths.extend(sorted(kb_dir.rglob("*.md")))

    for path in paths:
        metadata, body = parse_markdown(path)
        source = str(path)
        for generator in GENERATORS:
            examples.extend(generator(metadata, body, source))
    return examples


def dedupe_examples(examples: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    unique: list[dict[str, Any]] = []
    for ex in examples:
        key = json.dumps(ex["messages"], sort_keys=True)
        if key not in seen:
            seen.add(key)
            unique.append(ex)
    return unique


def split_data(
    examples: list[dict[str, Any]], val_ratio: float, test_ratio: float, seed: int
) -> tuple[list, list, list]:
    rng = random.Random(seed)
    data = examples.copy()
    rng.shuffle(data)
    n = len(data)
    n_test = int(n * test_ratio)
    n_val = int(n * val_ratio)
    return data[n_test + n_val :], data[n_test : n_test + n_val], data[:n_test]


def write_pretrain_corpus(examples: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for ex in examples:
            for msg in ex["messages"]:
                if msg["role"] in ("assistant", "system"):
                    handle.write(msg["content"].replace("\n", " ") + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare advanced training dataset")
    parser.add_argument("--kb-dir", type=Path, action="append", default=None)
    parser.add_argument("--output-dir", type=Path, default=Path("data/advanced"))
    parser.add_argument("--val-ratio", type=float, default=0.08)
    parser.add_argument("--test-ratio", type=float, default=0.02)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    kb_dirs = args.kb_dir or [
        Path("knowledge-base"),
        Path("knowledge-base/generated"),
    ]
    kb_dirs = [d for d in kb_dirs if d.exists()]

    examples = collect_examples(kb_dirs)
    examples = dedupe_examples(examples)
    train, val, test = split_data(examples, args.val_ratio, args.test_ratio, args.seed)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, rows in [("train", train), ("val", val), ("test", test)]:
        out = args.output_dir / f"{name}.jsonl"
        with out.open("w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    write_pretrain_corpus(examples, args.output_dir / "pretrain.txt")

    by_type: dict[str, int] = {}
    for ex in examples:
        t = ex["metadata"]["task_type"]
        by_type[t] = by_type.get(t, 0) + 1

    stats = {
        "total_examples": len(examples),
        "train": len(train),
        "val": len(val),
        "test": len(test),
        "by_task_type": by_type,
        "kb_dirs": [str(d) for d in kb_dirs],
    }
    (args.output_dir / "dataset_stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
