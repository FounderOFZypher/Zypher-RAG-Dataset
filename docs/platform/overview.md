# Coltex Platform Overview

**Coltex Mega RAG — The largest commercial RAG corpus (100,000,000+ sellable files)**

Coltex is a commercial mega-scale RAG product with a GraphRAG-native runtime.
The **Mega Dataset** (100M+ documents) is the primary sellable deliverable; the
**Coltex Runtime** indexes, retrieves, and operates over it.

```bash
make product-mega-smoke
python3 -m runtime status
```

Commercial docs: [product overview](../commercial/product-overview.md) · Runtime: [runtime.md](runtime.md)

---

## The shift

| Commodity RAG | Coltex Mega RAG |
|---------------|-----------------|
| Small curated dumps | **100,000,000+** sellable knowledge files |
| Flat vector index | GraphRAG hubs + typed relationships |
| One-off export | SKUs, marketplace packs, EULA |
| Store → Retrieve | Understand → Connect → Reason → Retrieve → Improve |
| Static corpus | Knowledge Lifecycle + Intelligence Engine |

The **Mega RAG commercial dataset** is the foundation deliverable. The **Knowledge Intelligence Engine** is the operational heart.

---

## Platform stack

```
┌─────────────────────────────────────────────────────────────────┐
│  Knowledge Studio · Governance · Lifecycle · Extensibility      │
├─────────────────────────────────────────────────────────────────┤
│  ★ Knowledge Intelligence Engine · Knowledge Health · AI Memory   │
├─────────────────────────────────────────────────────────────────┤
│  Reasoning Layer (intent → plan → retrieve → rank → evidence)   │
├─────────────────────────────────────────────────────────────────┤
│  Event Bus · Scheduler · Connectors · Plugins                   │
├─────────────────────────────────────────────────────────────────┤
│  Graph · Embeddings · Chunks · Trust & Provenance               │
├─────────────────────────────────────────────────────────────────┤
│  Dataset · Audit · Licensing  (available today)                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Core capabilities

### Available today

- **Mega RAG commercial product** — 100,000,000+ document target, commercial SKUs and packs
- **Advanced hybrid retrieval** — Vector, GraphRAG, BM25, Metadata, SQL, Code, API, Multi-Vector
- **Cross-encoder rerank + context compression** — production answer assembly
- **Explainable retrieval · incremental indexing · multi-workspace · plugins**
- **Streaming corpus pipeline** — `make product-mega` / `product-mega-smoke`
- **Knowledge graph** — hubs, routes, typed relationships, GraphRAG
- **Quality and audit** — distribution audit, EULA, benchmarks, provenance
- **Marketplace packs** — RAG core, languages, cloud, security, architecture

See [Advanced retrieval](advanced-retrieval.md) · [Intelligence Engine](intelligence-engine.md) · [Roadmap](roadmap.md)

### On the roadmap

- **Intelligence Engine** — discover, detect, recommend, improve
- **Knowledge Health** — operational dashboard scores
- **Event system and scheduler** — event-driven pipeline, automated jobs
- **Reasoning layer** — full intent-to-evidence pipeline
- **Knowledge lifecycle and AI governance** — state machine, retention, audit
- **Console, connectors, sync** — experience and integration layer

---

## Config manifests

| Manifest | Purpose |
|----------|---------|
| [events.yaml](../../config/events.yaml) | Event-driven pipeline |
| [knowledge-lifecycle.yaml](../../config/knowledge-lifecycle.yaml) | Document state machine |
| [scheduler.yaml](../../config/scheduler.yaml) | Automated maintenance jobs |
| [governance.yaml](../../config/governance.yaml) | Retention, access, audit |
| [extensibility.yaml](../../config/extensibility.yaml) | Plugins and hooks |
| [connectors.yaml](../../config/connectors.yaml) | Source connectors |

---

## Target buyers

| Segment | Primary value |
|---------|---------------|
| **AI / ML teams** | Instant 100M+ RAG corpus with GraphRAG edges |
| **Platform vendors** | Embed / resell licensed marketplace packs |
| **Enterprises** | Private Mega RAG + Knowledge OS governance |
| **Data marketplaces** | Shard sales under Coltex EULA |
| **Compliance / Legal** | Provenance, audit trail, retention policies |

---

## Related documents

- [Commercial product overview](../commercial/product-overview.md) — Mega RAG packaging
- [SKU matrix](../commercial/sku-matrix.md) — pricing & packs
- [Knowledge OS](knowledge-os.md) — platform vision
- [Intelligence Engine](intelligence-engine.md) — core intelligence architecture
- [Platform roadmap](roadmap.md) — feature specifications
