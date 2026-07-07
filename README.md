# Coltex

**Enterprise RAG Knowledge Corpus** — the largest connected retrieval-augmented generation dataset with multi-layer architecture, graph-linked domains, knowledge clusters, and procedural expansion to unlimited scale.

Coltex delivers a production-grade knowledge layer: 62+ domain folders, thousands of typed documents, cross-reference graph links, and a distributable export pipeline for commercial datasets.

---

## Knowledge Architecture

```
                    ┌─── L6 Meta (Catalog & governance) ───┐
                    │   L5 Executive (Context assembly)      │
                    │   L4 Reasoning (GraphRAG)             │
                    │   L3 Integration (Cluster assignment)  │
                    │   L2 Association (Metadata)           │
                    │   L1 Ingestion (Document intake)      │
                    └─────────────────┬─────────────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              ▼                       ▼                       ▼
         62+ Domains            18 Knowledge Hubs       4 Memory Tiers
              │                       │                       │
              └──────────► Graph Links + Pathways ◄──────────┘
                                   │
                    Vector + Metadata + GraphRouter
                                   │
                        brain retrieve / report
```

| Region | Path | Purpose |
|--------|------|---------|
| Processing layers | `knowledge-corpus/cortex/` | L1–L6 document processing stack |
| Functional clusters | `knowledge-corpus/lobes/` | Domain groupings by function |
| Domains | `knowledge-corpus/domains/` | 62+ technology categories |
| Knowledge hubs | `knowledge-corpus/hubs/` | 18 service-level clusters |
| Graph links | `knowledge-corpus/synapses/` | Hub-to-hub relationships |
| Pathways | `knowledge-corpus/pathways/` | Inter-cluster routes |
| Memory tiers | `knowledge-corpus/memory/` | Working, episodic, semantic, procedural |
| Quick reference | `knowledge-corpus/reflexes/` | FAQ index |

Architecture reference: [docs/architecture/knowledge-architecture.md](docs/architecture/knowledge-architecture.md)

---

## Quick Start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

make corpus-advanced
make index
python3 -m brain retrieve "What is GraphRAG?" --context
python3 -m brain report
```

---

## Expand the Corpus

| Command | Output |
|---------|--------|
| `make corpus-advanced` | Full architecture bootstrap (500 docs + pathways + hubs) |
| `make corpus-grow COUNT=1000` | Add 1,000 domain documents |
| `make corpus-mega` | 10,000 documents |
| `make generate-mega` | 100,000 procedural documents |
| `make generate-ultra` | 1,000,000 documents |

Catalog index: `data/brain/neural-map.json` · Architecture manifest: `data/brain/architecture-manifest.json`

---

## Retrieval Engine

Hybrid RAG pipeline with optional **GraphRouter** (region-aware graph expansion):

```bash
python3 -m brain index --reindex
python3 -m brain retrieve "<query>" --context
python3 -m brain stats
python3 -m brain report
```

---

## Premium Dataset Export

```bash
make product-premium-smoke   # 25,000 documents
make product-premium         # Full pipeline
make evaluate                # Benchmark evidence
```

---

## Documentation

- [Knowledge architecture](docs/architecture/knowledge-architecture.md)
- [Product setup](docs/product-setup.md)
- [Quality standards](docs/product-quality.md)
- [Evaluation guide](docs/product-evaluation.md)

---

## License

Licensed under the [End User License Agreement](EULA). Third-party dependencies in [NOTICE](NOTICE).
