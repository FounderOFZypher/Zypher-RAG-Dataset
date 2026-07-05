#!/usr/bin/env python3
"""Generate a massive, advanced knowledge corpus from templates and seed data."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import shutil
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus_templates import DOCUMENT_TYPES, TOPICS, Topic

CODE_SNIPPETS = {
    "python": '''```python
from typing import Any

class {class_name}:
    """{docstring}"""

    def __init__(self, config: dict[str, Any]) -> None:
        self._config = config
        self._cache: dict[str, Any] = {{}}

    def process(self, payload: dict[str, Any]) -> dict[str, Any]:
        key = payload.get("id", "default")
        if key in self._cache:
            return self._cache[key]
        result = {{"status": "ok", "topic": "{topic}", "variant": {variant}}}
        self._cache[key] = result
        return result
```''',
    "typescript": '''```typescript
interface {interface_name}Config {{
  topic: string;
  variant: number;
  retries: number;
}}

export async function {function_name}(config: {interface_name}Config): Promise<Record<string, unknown>> {{
  const backoff = Math.min(1000 * 2 ** config.retries, 30000);
  return {{
    status: "ok",
    topic: config.topic,
    variant: config.variant,
    backoffMs: backoff,
  }};
}}
```''',
    "sql": '''```sql
CREATE TABLE IF NOT EXISTS {table_name} (
    id          BIGSERIAL PRIMARY KEY,
    topic       TEXT NOT NULL,
    variant     INTEGER NOT NULL DEFAULT {variant},
    payload     JSONB NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_{table_name}_topic ON {table_name} (topic);
```''',
    "yaml": '''```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {service_name}
spec:
  replicas: {variant}
  template:
    spec:
      containers:
        - name: app
          image: zypher/{service_name}:{variant}
          resources:
            requests:
              cpu: "250m"
              memory: "512Mi"
```''',
}

PARAPHRASE_OPENERS = [
    "In practice,",
    "For production systems,",
    "When scaling to enterprise workloads,",
    "From first principles,",
    "Under high load,",
    "During incident response,",
    "For security-sensitive deployments,",
    "When integrating with legacy systems,",
]

SECTION_TEMPLATES = {
    "guide": ["Overview", "Prerequisites", "Core Concepts", "Implementation Steps", "Validation", "Next Steps"],
    "tutorial": ["Goal", "Setup", "Step-by-Step", "Common Mistakes", "Exercise", "Solution Walkthrough"],
    "faq": ["Question", "Short Answer", "Detailed Explanation", "When To Use", "Related Topics"],
    "troubleshooting": ["Symptoms", "Diagnostic Steps", "Root Causes", "Fix", "Prevention"],
    "api_reference": ["Endpoint", "Authentication", "Request Schema", "Response Schema", "Error Codes"],
    "code_walkthrough": ["Problem", "Approach", "Code", "Walkthrough", "Tests"],
    "architecture_decision": ["Context", "Options Considered", "Decision", "Consequences", "Review Date"],
    "runbook": ["Trigger", "Severity", "Immediate Actions", "Escalation", "Recovery Verification"],
    "deep_dive": ["Background", "Internals", "Trade-offs", "Benchmarks", "Expert Notes"],
    "comparison": ["Criteria", "Option A", "Option B", "Recommendation", "Migration Path"],
    "best_practices": ["Principles", "Do", "Don't", "Checklist", "Examples"],
    "anti_patterns": ["Pattern", "Why It Fails", "Real Example", "Better Alternative", "Detection"],
    "cheat_sheet": ["Quick Reference", "Commands", "Configs", "Snippets", "Pitfalls"],
    "interview_prep": ["Concept", "Junior Answer", "Senior Answer", "Follow-up Questions", "Red Flags"],
    "case_study": ["Scenario", "Constraints", "Solution", "Outcome", "Lessons Learned"],
}


@dataclass
class GeneratedDoc:
    doc_id: str
    path: Path
    category: str
    doc_type: str
    topic: str
    difficulty: str
    variant: int
    word_count: int


def _slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")[:80]


def _pascal_case(text: str) -> str:
    return "".join(part.capitalize() for part in re.split(r"[_\s-]+", text) if part)


def _render_code(topic: Topic, variant: int, lang: str) -> str:
    template = CODE_SNIPPETS[lang]
    class_name = _pascal_case(topic.slug)
    return template.format(
        class_name=class_name,
        interface_name=class_name,
        function_name=f"handle{_pascal_case(topic.slug)}",
        table_name=f"{topic.category}_{variant % 1000}",
        service_name=f"{topic.category}-svc",
        docstring=topic.title,
        topic=topic.slug,
        variant=variant,
    )


def _section_body(section: str, topic: Topic, doc_type: str, variant: int) -> str:
    opener = PARAPHRASE_OPENERS[variant % len(PARAPHRASE_OPENERS)]
    keywords = ", ".join(topic.keywords)
    return (
        f"{opener} **{section}** for `{topic.title}` ({doc_type}). "
        f"This variant {variant} covers {keywords} at {topic.difficulty} level. "
        f"Key considerations include reliability, observability, latency budgets, and safe rollout. "
        f"Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. "
        f"Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data."
    )


def build_document(topic: Topic, doc_type: str, variant: int, scale: int) -> tuple[str, dict[str, Any]]:
    doc_id = hashlib.sha1(f"{topic.slug}:{doc_type}:{variant}:{scale}".encode()).hexdigest()[:12]
    title = f"{topic.title} — {doc_type.replace('_', ' ').title()} (v{variant})"
    sections = SECTION_TEMPLATES.get(doc_type, SECTION_TEMPLATES["guide"])

    body_parts = [f"# {title}\n"]
    for section in sections:
        body_parts.append(f"\n## {section}\n\n{_section_body(section, topic, doc_type, variant)}")

    if doc_type in ("code_walkthrough", "tutorial", "guide", "api_reference"):
        lang = random.choice(["python", "typescript", "sql", "yaml"])
        body_parts.append(f"\n## Reference Implementation\n\n{_render_code(topic, variant, lang)}")

    if doc_type == "faq":
        body_parts.append(
            f"\n\n**Answer:** {topic.title} requires understanding {', '.join(topic.keywords)}. "
            f"Variant {variant} emphasizes operational excellence and measurable outcomes."
        )

    body = "".join(body_parts)
    metadata = {
        "id": doc_id,
        "title": title,
        "category": topic.category,
        "doc_type": doc_type,
        "topic_slug": topic.slug,
        "difficulty": topic.difficulty,
        "tags": list(topic.keywords) + [doc_type, topic.category, f"variant_{variant}"],
        "variant": variant,
        "scale": scale,
        "related": [],
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "version": "2.0",
    }
    return body, metadata


def write_document(output_dir: Path, topic: Topic, doc_type: str, variant: int, scale: int) -> GeneratedDoc:
    body, metadata = build_document(topic, doc_type, variant, scale)
    doc_id = metadata["id"]
    filename = f"{doc_id}_{topic.category}_{doc_type}_v{variant:04d}.md"
    path = output_dir / topic.category / doc_type / filename

    frontmatter = yaml.safe_dump(metadata, sort_keys=False).strip()
    content = f"---\n{frontmatter}---\n\n{body}\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

    return GeneratedDoc(
        doc_id=doc_id,
        path=path,
        category=topic.category,
        doc_type=doc_type,
        topic=topic.slug,
        difficulty=topic.difficulty,
        variant=variant,
        word_count=len(body.split()),
    )


def _generate_job(args: tuple[str, str, str, str, int, int, str]) -> dict[str, Any]:
    topic_slug, topic_title, category, difficulty, keywords, variant, doc_type, scale_str, output_str = args
    topic = Topic(topic_slug, topic_title, category, difficulty, tuple(keywords.split("|")))
    scale = int(scale_str)
    output_dir = Path(output_str)
    doc = write_document(output_dir, topic, doc_type, variant, scale)
    return {
        "doc_id": doc.doc_id,
        "path": str(doc.path),
        "category": doc.category,
        "doc_type": doc.doc_type,
        "topic": doc.topic,
        "difficulty": doc.difficulty,
        "variant": doc.variant,
        "word_count": doc.word_count,
    }


def copy_seed_corpus(seed_dir: Path, output_dir: Path) -> int:
    seed_out = output_dir / "_seed"
    seed_out.mkdir(parents=True, exist_ok=True)
    count = 0

    # Copy only original seed content, never generated/
    patterns = ["CHUNK-*.md", "configs/*", "schemas/*", "openapi/*", "kubernetes/*", "docker-compose/*"]
    for pattern in patterns:
        for path in seed_dir.glob(pattern):
            if "generated" in path.parts:
                continue
            rel = path.relative_to(seed_dir)
            dest = seed_out / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            if path.is_dir():
                continue
            shutil.copy2(path, dest)
            count += 1
    return count


def build_jobs(
    topics: list[Topic],
    doc_types: list[str],
    variations: int,
    scale: int,
    output_dir: Path,
) -> list[tuple]:
    # scale=1000 with variations=12 → 12 variants per topic/doc_type (~112k files)
    effective_variants = max(1, int(variations * scale / 1000))
    jobs = []
    for topic in topics:
        for doc_type in doc_types:
            for variant in range(effective_variants):
                jobs.append(
                    (
                        topic.slug,
                        topic.title,
                        topic.category,
                        topic.difficulty,
                        "|".join(topic.keywords),
                        variant,
                        doc_type,
                        str(scale),
                        str(output_dir),
                    )
                )
    return jobs


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate advanced knowledge-base corpus at scale")
    parser.add_argument("--config", type=Path, default=Path("config/corpus_generation.yaml"))
    parser.add_argument("--scale", type=int, default=None, help="Override scale multiplier")
    parser.add_argument("--variations", type=int, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--seed-dir", type=Path, default=None)
    parser.add_argument("--workers", type=int, default=None)
    parser.add_argument("--max-files", type=int, default=0, help="Cap total generated files (0=unlimited)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    with args.config.open(encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle)

    scale = args.scale if args.scale is not None else int(cfg.get("scale", 1000))
    variations = args.variations if args.variations is not None else int(cfg.get("variations_per_doc", 12))
    output_dir = args.output_dir or Path(cfg.get("output_dir", "knowledge-base/generated"))
    seed_dir = args.seed_dir or Path(cfg.get("seed_dir", "knowledge-base"))
    workers = args.workers or int(cfg.get("parallel_workers", 4))
    doc_types = cfg.get("document_types", DOCUMENT_TYPES)
    categories = set(cfg.get("categories", []))

    topics = [t for t in TOPICS if t.category in categories] if categories else TOPICS
    jobs = build_jobs(topics, doc_types, variations, scale, output_dir)
    if args.max_files and len(jobs) > args.max_files:
        jobs = jobs[: args.max_files]

    print(f"Topics: {len(topics)}")
    print(f"Document types: {len(doc_types)}")
    print(f"Scale: {scale}, variations: {variations}")
    print(f"Planned files: {len(jobs):,}")

    if args.dry_run:
        return

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    seed_count = copy_seed_corpus(seed_dir, output_dir)
    print(f"Copied {seed_count} seed files to {output_dir / '_seed'}")

    catalog: list[dict[str, Any]] = []
    completed = 0

    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(_generate_job, job) for job in jobs]
        for future in as_completed(futures):
            catalog.append(future.result())
            completed += 1
            if completed % 5000 == 0:
                print(f"Generated {completed:,} / {len(jobs):,} files...")

    catalog.sort(key=lambda row: row["path"])
    catalog_path = output_dir / "catalog.json"
    stats = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_files": len(catalog) + seed_count,
        "generated_files": len(catalog),
        "seed_files": seed_count,
        "scale": scale,
        "variations_per_doc": variations,
        "topics": len(topics),
        "document_types": len(doc_types),
        "categories": sorted({row["category"] for row in catalog}),
        "by_category": {},
        "by_doc_type": {},
    }
    for row in catalog:
        stats["by_category"][row["category"]] = stats["by_category"].get(row["category"], 0) + 1
        stats["by_doc_type"][row["doc_type"]] = stats["by_doc_type"].get(row["doc_type"], 0) + 1

    catalog_path.write_text(
        json.dumps({"stats": stats, "files": catalog}, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(stats, indent=2))
    print(f"Catalog written to {catalog_path}")


if __name__ == "__main__":
    main()
