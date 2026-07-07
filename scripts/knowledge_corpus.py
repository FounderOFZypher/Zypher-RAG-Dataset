#!/usr/bin/env python3
"""
Coltex Knowledge Corpus — build, organize, and wire the enterprise knowledge dataset.

Creates domain folders, knowledge clusters, graph links, and a catalog manifest.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from brain_schema import CATEGORIES, KNOWLEDGE_HUBS
from brain_architecture import (
    PATHWAY_TYPES,
    brain_lobes,
    cortex_layers,
    domain_to_lobe,
    hub_registry,
    load_architecture,
    memory_tiers,
)
from corpus_templates import TOPICS
from expand_curated_kb import (
    CURATED_DOC_TYPES,
    _chunk_id,
    _existing_chunk_max,
    _format_chunk_markdown,
    _slugify,
    iter_curated_jobs,
)
from generate_corpus import build_document

CORPUS_ROOT = ROOT / "knowledge-base" / "knowledge-corpus"
NEURAL_MAP_PATH = ROOT / "data" / "brain" / "neural-map.json"
ARCHITECTURE_PATH = ROOT / "data" / "brain" / "architecture-manifest.json"

PATHWAY_TEMPLATE = """---
id: PATHWAY-{pathway_id}
title: "Domain Pathway: {source_lobe} → {target_lobe} ({pathway_type})"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: {source_lobe}
lobe_target: {target_lobe}
pathway_type: {pathway_type}
tags: [pathway, {pathway_type}, {source_lobe}, {target_lobe}]
related: [{source_anchor}, {target_anchor}]
see_also: [{source_anchor}, {target_anchor}]
synthesizes: [{source_anchor}]
---

# Domain Pathway: {source_lobe} → {target_lobe}

**Type:** `{pathway_type}` · **Tier:** association layer

## Route
Documents in lobe `{source_lobe}` connect to lobe `{target_lobe}` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `{source_anchor}` ({source_lobe})
- Target: `{target_anchor}` ({target_lobe})

## Coltex Knowledge Architecture
Region-aware graph routing (`GraphRouter`) prioritizes documents in `/pathways/` during GraphRAG expansion.
"""

HUB_ANCHOR_TEMPLATE = """---
id: HUB-{hub_slug_upper}
title: "Knowledge Cluster: {hub_title}"
doc_type: architecture_decision
category: {category}
hub: {hub_slug}
lobe: {lobe}
tags: [hub, knowledge-cluster, {hub_slug}]
see_also: [CORTEX-00001]
---

# {hub_title}

Central knowledge cluster for the Coltex corpus.

## Components
{components}

## Lobe assignment
**{lobe}** lobe · tier `{tier}`

## Document types in this hub
{doc_types}

## GraphRAG
All documents with `hub: {hub_slug}` form a traversable cluster.
Synapses and pathways connect this hub to other neural clusters.
"""

DOMAIN_README = """# {name} Domain

Part of the **Coltex Knowledge Corpus** — `{category}` knowledge cluster.

Documents here are auto-generated, graph-linked, and indexed by Coltex.
Each file carries typed metadata (`doc_type`, `hub`, `related`) for GraphRAG traversal.

## Stats
- Category: `{category}`
- Parent: `knowledge-corpus/domains/{category}/`

Query this domain:
```bash
python3 -m brain retrieve "your question about {category}"
```
"""

HUB_README = """# {title}

Knowledge cluster `{slug}` — documents sharing `hub: {slug}` metadata.

## Components
{components}

## Linked doc types
{doc_types}
"""

SYNAPSE_TEMPLATE = """---
id: SYNAPSE-{synapse_id}
title: "Graph Link: {source_hub} ↔ {target_hub}"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, {source_hub}, {target_hub}]
related: [{source_doc}, {target_doc}]
see_also: [{source_doc}, {target_doc}]
depends_on: [{source_doc}]
---

# Graph Link: {source_hub} → {target_hub}

Cross-domain connection in the Coltex knowledge graph.

## Connection type
**{relation}** — documents in `{source_hub}` {relation_desc} `{target_hub}`.

## Source hub
- Hub: `{source_hub}`
- Anchor: `{source_doc}`

## Target hub
- Hub: `{target_hub}`
- Anchor: `{target_doc}`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex note
Graph links are first-class edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
"""


def _ensure_structure() -> dict[str, Path]:
    """Create advanced knowledge-corpus folder tree (Knowledge Architecture v2)."""
    cfg = load_architecture()
    dirs: dict[str, Path] = {
        "root": CORPUS_ROOT,
        "domains": CORPUS_ROOT / "domains",
        "hubs": CORPUS_ROOT / "hubs",
        "synapses": CORPUS_ROOT / "synapses",
        "pathways": CORPUS_ROOT / "pathways",
        "cortex": CORPUS_ROOT / "cortex",
        "memory": CORPUS_ROOT / "memory",
        "reflexes": CORPUS_ROOT / "reflexes",
        "lobes": CORPUS_ROOT / "lobes",
        "hippocampus": CORPUS_ROOT / "hippocampus",
        "cerebellum": CORPUS_ROOT / "cerebellum",
        "brainstem": CORPUS_ROOT / "brainstem",
        "thalamus": CORPUS_ROOT / "thalamus",
        "amygdala": CORPUS_ROOT / "amygdala",
    }
    for key, path in list(dirs.items()):
        if key in ("root",):
            continue
        path.mkdir(parents=True, exist_ok=True)

    # Cortical layers L1–L6
    for layer in cortex_layers(cfg):
        layer_path = CORPUS_ROOT / layer.path
        layer_path.mkdir(parents=True, exist_ok=True)
        readme = layer_path / "README.md"
        if not readme.exists():
            readme.write_text(
                f"# Cortex {layer.slug}\n\n**Role:** {layer.role}\n\n**Latency target:** {layer.latency_ms}ms\n",
                encoding="utf-8",
            )

    # Brain lobes
    lobe_paths: dict[str, Path] = {}
    for lobe in brain_lobes(cfg):
        lp = CORPUS_ROOT / lobe.path
        lp.mkdir(parents=True, exist_ok=True)
        lobe_paths[lobe.slug] = lp
        readme = lp / "README.md"
        if not readme.exists():
            domains = ", ".join(lobe.domains) or "cross-domain"
            readme.write_text(
                f"# {lobe.slug.title()} Lobe\n\n**Role:** {lobe.role}\n\n**Domains:** {domains}\n",
                encoding="utf-8",
            )

    # Memory tiers
    for tier in memory_tiers(cfg):
        mp = CORPUS_ROOT / tier.path
        mp.mkdir(parents=True, exist_ok=True)
        readme = mp / "README.md"
        if not readme.exists():
            cap = tier.capacity_docs or "unlimited"
            readme.write_text(
                f"# Memory: {tier.slug}\n\n**Role:** {tier.role}\n\n**Capacity:** {cap} docs\n",
                encoding="utf-8",
            )

    # Domain folders — all categories + lobe-mapped domains
    d2l = domain_to_lobe(cfg)
    all_domains = sorted(set(list(d2l.keys()) + list(CATEGORIES)))
    domain_paths: dict[str, Path] = {}
    for cat in all_domains:
        d = dirs["domains"] / cat
        d.mkdir(parents=True, exist_ok=True)
        readme = d / "README.md"
        lobe = d2l.get(cat, "general")
        if not readme.exists():
            readme.write_text(
                DOMAIN_README.format(name=cat.replace("_", " ").title(), category=cat)
                + f"\n\n**Lobe:** `{lobe}`\n",
                encoding="utf-8",
            )
        domain_paths[cat] = d

    # Hub folders
    hub_paths: dict[str, Path] = {}
    registry = {e.slug: e for e in hub_registry(cfg)}
    for hub in KNOWLEDGE_HUBS:
        h = dirs["hubs"] / hub.slug
        h.mkdir(parents=True, exist_ok=True)
        readme = h / "README.md"
        if not readme.exists():
            components = "\n".join(f"- {c}" for c in hub.components)
            doc_types = ", ".join(hub.doc_types)
            entry = registry.get(hub.slug)
            lobe_info = f"\n\n**Lobe:** `{entry.lobe}` · **Tier:** `{entry.tier}`" if entry else ""
            readme.write_text(
                HUB_README.format(
                    title=hub.title,
                    slug=hub.slug,
                    components=components,
                    doc_types=doc_types,
                )
                + lobe_info,
                encoding="utf-8",
            )
        hub_paths[hub.slug] = h

    cortex_manifest = dirs["cortex"] / "L6-meta" / "BRAIN_IDENTITY.md"
    cortex_manifest.parent.mkdir(parents=True, exist_ok=True)
    if not cortex_manifest.exists():
        cortex_manifest.write_text(_cortex_identity(), encoding="utf-8")

    root_readme = CORPUS_ROOT / "README.md"
    root_readme.write_text(_knowledge_corpus_readme(), encoding="utf-8")

    dirs["domain_paths"] = domain_paths  # type: ignore
    dirs["hub_paths"] = hub_paths  # type: ignore
    dirs["lobe_paths"] = lobe_paths  # type: ignore
    return dirs


def _cortex_identity() -> str:
    return """---
id: CORTEX-00001
title: Coltex Knowledge Architecture — Knowledge Corpus Identity
doc_type: deep_dive
category: rag
hub: coltex_knowledge_core
lobe: frontal
tags: [cortex, identity, knowledge-corpus, knowledge_architecture]
---

# Coltex Knowledge Architecture v2

The meta-layer of Coltex — a **multi-tier knowledge architecture** for enterprise-scale RAG datasets.

## Processing tiers
| Tier | Regions |
|------|---------|
| Ingestion (L1) | Raw document intake, chunk signals |
| Association (L2-L4) | Domain linking, cluster assignment, GraphRAG |
| Executive (L5-L6) | Context assembly, meta-reasoning |
| Operations | Quick reference, runbooks, health checks |

## Functional clusters
| Cluster | Role |
|---------|------|
| Architecture | ADRs, agentic systems, API design |
| Retrieval | RAG, embeddings, LLM integration |
| Data | SQL, vectors, indexing |
| Operations | Observability, MLOps |
| Security | Access control, incidents, compliance |
| Automation | CI/CD, infrastructure |

## Corpus report
```bash
python3 -m brain report
make corpus-report
```
"""


def _knowledge_corpus_readme() -> str:
    return """# Coltex Knowledge Architecture

Enterprise RAG knowledge corpus with **6 processing layers**, **10 functional clusters**, **4 memory tiers**, **18 knowledge hubs**, and **millions of graph edges**.

## Structure
```
knowledge-corpus/
├── cortex/L1-sensory … L6-meta    # Processing layers
├── lobes/                           # Functional clusters
├── domains/                         # 62+ technology domains
├── hubs/                            # 18 knowledge clusters
├── synapses/                        # Hub-to-hub graph links
├── pathways/                        # Inter-cluster routes
├── memory/                          # Tiered retention stores
└── reflexes/                        # Quick-reference FAQs
```

## Build
```bash
make corpus-advanced              # Full architecture bootstrap
make corpus-grow COUNT=1000       # Add domain documents
make corpus-mega                  # 10,000 documents
```

## Query
```bash
make index
python3 -m brain report
python3 -m brain retrieve "Explain domain pathway routing" --context
```
"""


def grow_domains(count: int, dry_run: bool = False) -> dict:
    """Generate documents into domain folders."""
    structure = _ensure_structure()
    domain_paths: dict[str, Path] = structure["domain_paths"]  # type: ignore

    start_num = _existing_chunk_max() + 1
    # Also scan knowledge-corpus for max chunk
    for path in CORPUS_ROOT.rglob("CHUNK-*.md"):
        m = re.match(r"CHUNK-(\d+)", path.name)
        if m:
            start_num = max(start_num, int(m.group(1)) + 1)

    jobs = iter_curated_jobs(count, start_num)
    written = 0
    by_domain: dict[str, int] = {}

    for chunk_num, topic, doc_type, variant in jobs:
        body, metadata = build_document(topic, doc_type, variant, scale=1000)
        metadata["hub"] = metadata.get("hub") or topic.hub or f"domain_{topic.category}"
        related = [_chunk_id(chunk_num - i) for i in range(1, min(4, chunk_num - start_num + 1))]
        content = _format_chunk_markdown(chunk_num, body, metadata, related)

        domain_dir = domain_paths.get(topic.category) or (structure["domains"] / topic.category)
        domain_dir.mkdir(parents=True, exist_ok=True)

        slug = _slugify(metadata["title"])
        filename = f"CHUNK-{chunk_num:05d}-{slug}.md"
        path = domain_dir / filename

        if not dry_run:
            path.write_text(content, encoding="utf-8")
        written += 1
        by_domain[topic.category] = by_domain.get(topic.category, 0) + 1

    return {
        "documents_written": written,
        "start_chunk": start_num,
        "end_chunk": start_num + written - 1 if written else start_num,
        "domains_touched": len(by_domain),
        "by_domain": by_domain,
        "dry_run": dry_run,
    }


def wire_synapses(dry_run: bool = False) -> dict:
    """Create synapse documents linking knowledge hubs."""
    structure = _ensure_structure()
    synapse_dir: Path = structure["synapses"]
    hubs = KNOWLEDGE_HUBS
    written = 0
    synapse_ids: list[str] = []

    relations = [
        ("depends_on", "depends on"),
        ("see_also", "is related to"),
        ("calls", "calls into"),
        ("documents", "documents"),
    ]

    for i, source in enumerate(hubs):
        for j, target in enumerate(hubs):
            if source.slug == target.slug:
                continue
            relation, relation_desc = relations[(i + j) % len(relations)]
            synapse_num = i * len(hubs) + j
            synapse_id = f"{synapse_num:05d}"
            source_doc = f"HUB-{source.slug.upper().replace('-', '_')}"
            target_doc = f"HUB-{target.slug.upper().replace('-', '_')}"

            content = SYNAPSE_TEMPLATE.format(
                synapse_id=synapse_id,
                source_hub=source.slug,
                target_hub=target.slug,
                source_doc=source_doc,
                target_doc=target_doc,
                relation=relation,
                relation_desc=relation_desc,
            )
            path = synapse_dir / f"SYNAPSE-{synapse_id}-{source.slug}-to-{target.slug}.md"
            if not dry_run:
                path.write_text(content, encoding="utf-8")
            written += 1
            synapse_ids.append(f"SYNAPSE-{synapse_id}")

    return {"synapses_written": written, "synapse_ids": synapse_ids[:10], "dry_run": dry_run}


def seed_reflexes(dry_run: bool = False) -> dict:
    """Fast-path reflex documents (instant-recall FAQs)."""
    structure = _ensure_structure()
    reflex_dir: Path = structure["reflexes"]
    prompts = [
        ("What is Coltex?", "Coltex is an enterprise RAG knowledge corpus with hybrid retrieval."),
        ("What is GraphRAG?", "GraphRAG expands vector hits via typed document relationship edges."),
        ("How do I query the corpus?", "python3 -m brain retrieve \"your question\" --context"),
        ("How do I expand the corpus?", "make corpus-grow COUNT=500"),
        ("What is a graph link?", "A cross-hub edge in knowledge-corpus/synapses/."),
    ]
    written = 0
    for i, (q, a) in enumerate(prompts):
        content = f"""---
id: REFLEX-{i:05d}
title: "{q}"
doc_type: faq
category: rag
hub: coltex_knowledge_core
tags: [reflex, faq, instant-recall]
---

# {q}

{a}

## Reflex path
Quick-reference nodes optimized for common queries during corpus reporting and retrieval.
"""
        path = reflex_dir / f"REFLEX-{i:05d}-{ _slugify(q) }.md"
        if not dry_run:
            path.write_text(content, encoding="utf-8")
        written += 1
    return {"reflexes_written": written, "dry_run": dry_run}


def wire_pathways(dry_run: bool = False) -> dict:
    """Create inter-lobe neural pathway documents."""
    structure = _ensure_structure()
    pathway_dir: Path = structure["pathways"]
    lobes = brain_lobes()
    written = 0

    for i, source in enumerate(lobes):
        for j, target in enumerate(lobes):
            if source.slug == target.slug:
                continue
            pathway_type = PATHWAY_TYPES[(i + j) % len(PATHWAY_TYPES)]
            pid = f"{i:02d}{j:02d}"
            source_anchor = f"LOBE-{source.slug.upper()}"
            target_anchor = f"LOBE-{target.slug.upper()}"
            content = PATHWAY_TEMPLATE.format(
                pathway_id=pid,
                source_lobe=source.slug,
                target_lobe=target.slug,
                pathway_type=pathway_type,
                source_anchor=source_anchor,
                target_anchor=target_anchor,
            )
            path = pathway_dir / f"PATHWAY-{pid}-{source.slug}-to-{target.slug}.md"
            if not dry_run:
                path.write_text(content, encoding="utf-8")
            written += 1

    return {"pathways_written": written, "dry_run": dry_run}


def seed_hub_anchors(dry_run: bool = False) -> dict:
    """Anchor document per neural hub."""
    structure = _ensure_structure()
    registry = {e.slug: e for e in hub_registry()}
    written = 0

    for hub in KNOWLEDGE_HUBS:
        entry = registry.get(hub.slug)
        lobe = entry.lobe if entry else "frontal"
        tier = entry.tier if entry else "association"
        components = "\n".join(f"- {c}" for c in hub.components)
        doc_types = ", ".join(hub.doc_types)
        content = HUB_ANCHOR_TEMPLATE.format(
            hub_slug_upper=hub.slug.upper().replace("-", "_"),
            hub_title=hub.title,
            hub_slug=hub.slug,
            category=hub.category,
            lobe=lobe,
            tier=tier,
            components=components,
            doc_types=doc_types,
        )
        path = structure["hub_paths"][hub.slug] / f"HUB-ANCHOR-{hub.slug}.md"  # type: ignore
        if not dry_run:
            path.write_text(content, encoding="utf-8")
        written += 1

    return {"hub_anchors_written": written, "dry_run": dry_run}


def seed_cortex_layers(dry_run: bool = False) -> dict:
    """One architecture blueprint per cortical layer."""
    cfg = load_architecture()
    written = 0
    for i, layer in enumerate(cortex_layers(cfg)):
        content = f"""---
id: CORTEX-L{i + 1}
title: "Cortical Layer {layer.slug}"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [cortex, {layer.slug}, knowledge_architecture]
---

# Cortical Layer: {layer.slug}

**Role:** {layer.role}

## Processing latency target
{layer.latency_ms}ms

## Path
`{layer.path}`

## Integration
Layer {layer.slug} feeds forward into the next cortical layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during neural routing.
"""
        layer_path = CORPUS_ROOT / layer.path / f"CORTEX-LAYER-{layer.slug}.md"
        if not dry_run:
            layer_path.write_text(content, encoding="utf-8")
        written += 1
    return {"cortex_layers_written": written, "dry_run": dry_run}


def seed_memory_samples(dry_run: bool = False) -> dict:
    """Seed sample documents in each memory tier."""
    written = 0
    samples = [
        ("working", "Active query context buffer", "working memory for current retrieval session"),
        ("episodic", "Incident timeline 2026-07-07", "episodic record of indexing pipeline degradation"),
        ("semantic", "GraphRAG edge type taxonomy", "stable semantic fact about relationship types"),
        ("procedural", "Index rebuild runbook", "procedural steps for full brain reindex"),
    ]
    for tier_slug, title, body in samples:
        for tier in memory_tiers():
            if tier.slug != tier_slug:
                continue
            content = f"""---
id: MEMORY-{tier_slug.upper()}
title: "{title}"
doc_type: guide
category: memory
hub: coltex_knowledge_core
memory_tier: {tier_slug}
tags: [memory, {tier_slug}]
---

# {title}

{body}

## Memory tier: {tier_slug}
**Role:** {tier.role}
"""
            path = CORPUS_ROOT / tier.path / f"MEMORY-{tier_slug}-sample.md"
            if not dry_run:
                path.write_text(content, encoding="utf-8")
            written += 1
    return {"memory_samples_written": written, "dry_run": dry_run}


def build_architecture_manifest() -> dict:
    """Write architecture-manifest.json alongside neural-map."""
    cfg = load_architecture()
    arch = cfg.get("architecture", {})
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "codename": arch.get("codename", "knowledge_architecture"),
        "version": arch.get("version", "2.0"),
        "cortex_layers": len(cortex_layers(cfg)),
        "lobes": len(brain_lobes(cfg)),
        "memory_tiers": len(memory_tiers(cfg)),
        "hubs": len(KNOWLEDGE_HUBS),
        "pathway_types": len(PATHWAY_TYPES),
        "relationship_types": len(cfg.get("relationship_types", {}).get("core", []))
        + len(cfg.get("relationship_types", {}).get("advanced", [])),
        "scale_targets": cfg.get("scale", {}),
        "lobe_registry": [
            {"slug": l.slug, "domains": list(l.domains), "role": l.role}
            for l in brain_lobes(cfg)
        ],
    }
    ARCHITECTURE_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARCHITECTURE_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


def build_neural_map() -> dict:
    """Scan entire knowledge base and write neural-map.json manifest."""
    kb_root = ROOT / "knowledge-base"
    domains: dict[str, int] = {}
    hubs: dict[str, int] = {}
    doc_types: dict[str, int] = {}
    total = 0
    synapses = 0
    reflexes = 0
    pathways = 0
    lobes: dict[str, int] = {}
    cortex_layer_counts: dict[str, int] = {}
    memory_counts: dict[str, int] = {}

    for path in kb_root.rglob("*.md"):
        if "_excluded" in path.parts or "_seed" in path.parts:
            continue
        total += 1
        parts = path.parts
        if "synapses" in parts:
            synapses += 1
        if "reflexes" in parts:
            reflexes += 1
        if "pathways" in parts:
            pathways += 1
        if "lobes" in parts:
            idx = parts.index("lobes") if "lobes" in parts else -1
            if idx >= 0 and idx + 1 < len(parts):
                lobes[parts[idx + 1]] = lobes.get(parts[idx + 1], 0) + 1
        if "cortex" in parts:
            for p in parts:
                if p.startswith("L") and "-" in p:
                    cortex_layer_counts[p] = cortex_layer_counts.get(p, 0) + 1
        if "memory" in parts:
            idx = list(parts).index("memory") if "memory" in parts else -1
            if idx >= 0 and idx + 1 < len(parts):
                memory_counts[parts[idx + 1]] = memory_counts.get(parts[idx + 1], 0) + 1
        if "domains" in parts:
            parts = path.parts
            idx = parts.index("domains")
            if idx + 1 < len(parts):
                cat = parts[idx + 1]
                domains[cat] = domains.get(cat, 0) + 1
        try:
            text = path.read_text(encoding="utf-8")[:2000]
            if "hub:" in text:
                for line in text.splitlines():
                    if line.strip().startswith("hub:"):
                        hub = line.split(":", 1)[1].strip().strip('"')
                        hubs[hub] = hubs.get(hub, 0) + 1
                        break
            if "doc_type:" in text:
                for line in text.splitlines():
                    if line.strip().startswith("doc_type:"):
                        dt = line.split(":", 1)[1].strip().strip('"')
                        doc_types[dt] = doc_types.get(dt, 0) + 1
                        break
        except OSError:
            pass

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "brain": "coltex-knowledge_architecture",
        "architecture_version": "2.0",
        "codename": "knowledge_architecture",
        "total_documents": total,
        "domains": domains,
        "domain_count": len(domains),
        "hubs": hubs,
        "hub_count": len(hubs),
        "lobes": lobes,
        "lobe_count": len(lobes),
        "cortex_layers": cortex_layer_counts,
        "memory_tiers": memory_counts,
        "doc_types": doc_types,
        "synapses": synapses,
        "pathways": pathways,
        "reflexes": reflexes,
        "categories_available": len(CATEGORIES),
        "topics_available": len(TOPICS),
        "hubs_registered": len(KNOWLEDGE_HUBS),
    }

    NEURAL_MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
    NEURAL_MAP_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    build_architecture_manifest()
    return manifest


def bootstrap_advanced(grow: int = 500, dry_run: bool = False) -> dict:
    """Knowledge Architecture v2 full bootstrap."""
    _ensure_structure()
    grow_stats = grow_domains(grow, dry_run=dry_run) if grow > 0 else {}
    return {
        "bootstrap": "knowledge_architecture-v2",
        "structure": True,
        "grow": grow_stats,
        "synapses": wire_synapses(dry_run=dry_run),
        "pathways": wire_pathways(dry_run=dry_run),
        "hub_anchors": seed_hub_anchors(dry_run=dry_run),
        "cortex_layers": seed_cortex_layers(dry_run=dry_run),
        "memory": seed_memory_samples(dry_run=dry_run),
        "reflexes": seed_reflexes(dry_run=dry_run),
        "neural_map": {
            "total_documents": build_neural_map().get("total_documents") if not dry_run else 0,
            "path": str(NEURAL_MAP_PATH),
            "architecture_manifest": str(ARCHITECTURE_PATH),
        },
        "dry_run": dry_run,
    }


def bootstrap(grow: int = 300, dry_run: bool = False) -> dict:
    """Full knowledge corpus bootstrap: structure + grow + synapses + reflexes + map."""
    return bootstrap_advanced(grow=grow, dry_run=dry_run)


def main() -> None:
    parser = argparse.ArgumentParser(description="Coltex Knowledge Corpus orchestrator")
    sub = parser.add_subparsers(dest="command", required=True)

    p_boot = sub.add_parser("bootstrap", help="Scaffold + grow + wire + neural map")
    p_boot.add_argument("--grow", type=int, default=300)
    p_boot.add_argument("--dry-run", action="store_true")

    p_grow = sub.add_parser("grow", help="Grow domain documents")
    p_grow.add_argument("--count", type=int, default=200)
    p_grow.add_argument("--dry-run", action="store_true")

    sub.add_parser("structure", help="Create folder tree only")
    sub.add_parser("synapses", help="Wire hub synapses")
    sub.add_parser("reflexes", help="Seed reflex FAQs")
    sub.add_parser("map", help="Rebuild neural-map.json")

    sub.add_parser("pathways", help="Wire inter-lobe neural pathways")
    sub.add_parser("hubs", help="Seed hub anchor documents")
    sub.add_parser("cortex", help="Seed cortical layer blueprints")
    sub.add_parser("memory", help="Seed memory tier samples")

    p_adv = sub.add_parser("advanced", help="Full Knowledge Architecture v2 bootstrap")
    p_adv.add_argument("--grow", type=int, default=500)
    p_adv.add_argument("--dry-run", action="store_true")

    args = parser.parse_args()

    if args.command == "bootstrap":
        result = bootstrap(grow=args.grow, dry_run=args.dry_run)
    elif args.command == "advanced":
        result = bootstrap_advanced(grow=args.grow, dry_run=args.dry_run)
    elif args.command == "grow":
        _ensure_structure()
        result = grow_domains(args.count, dry_run=args.dry_run)
        if not args.dry_run:
            result["neural_map"] = build_neural_map()
    elif args.command == "structure":
        result = {"structure": str(_ensure_structure()["root"])}
    elif args.command == "synapses":
        result = wire_synapses()
        result["neural_map"] = build_neural_map()
    elif args.command == "reflexes":
        result = seed_reflexes()
        result["neural_map"] = build_neural_map()
    elif args.command == "map":
        result = build_neural_map()
    elif args.command == "pathways":
        result = wire_pathways()
        result["neural_map"] = build_neural_map()
    elif args.command == "hubs":
        result = seed_hub_anchors()
        result["neural_map"] = build_neural_map()
    elif args.command == "cortex":
        result = seed_cortex_layers()
        result["neural_map"] = build_neural_map()
    elif args.command == "memory":
        result = seed_memory_samples()
        result["neural_map"] = build_neural_map()
    else:
        result = {"error": "unknown command"}

    print(yaml.safe_dump(result, sort_keys=False))


if __name__ == "__main__":
    main()
