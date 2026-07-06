# Zypher Mega RAG Database

A **$1000+ premium RAG dataset** and retrieval engine. Original synthetic documents, vector-ready chunks, embeddings, graph relationships, metadata, benchmarks, and evaluation — nothing else.

No chatbot. No LLM hosting. No fine-tuning. No REST API. **Database only.**

## What this is

```
┌─────────────────────────────────────────────────────────────┐
│                   ZYPHER MEGA RAG DATABASE                    │
│                                                             │
│  Knowledge Base · Chunks · Embeddings · Graph · Metadata    │
│  Catalog · Benchmarks · Evaluation · Distribution Audit     │
└─────────────────────────────────────────────────────────────┘
```

| Artifact | Path |
|----------|------|
| Vector-ready chunks | `data/product/chunks/chunks.jsonl` |
| Document catalog | `data/product/catalog.jsonl` |
| Embeddings | `data/product/embeddings/embeddings.jsonl` |
| Graph edges | `data/product/graph/edges.jsonl` |
| Metadata index | `data/product/metadata/documents.json` |
| Benchmarks | `benchmarks/*.jsonl` |
| Manifest | `data/product/manifest.json` |

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Build premium dataset (10K smoke test)
make product-premium-smoke

# Query the brain index
make index
python3 -m brain retrieve "What is RAG for code?" --context
```

## Premium tiers ($1000+ dataset)

| Tier | Command | Scale |
|------|---------|-------|
| Smoke | `make product-premium-smoke` | 10,000 documents |
| Premium | `make product-premium` | Config default |
| **Hyper** | `make product-hyper` | **100B× multiplier — uncapped** |

Hyper tier: `mega_multiplier: 100000000000` — procedural streaming, 604+ trillion unique document combinations.

```bash
# Full hyper run (Vast.ai / cluster)
make product-hyper
```

## Brain module (retrieval engine)

```
brain/
├── brain.py           # ZypherBrain database engine
├── ingestion/         # Load documents
├── embeddings/        # Vector encoding
├── indexing/          # ChromaDB vector store
├── metadata/          # Filters by doc_type, category, tags
├── graph/             # Typed relationship traversal
├── reranking/         # Merge + score results
└── retrieval/         # Full retrieval pipeline
```

```bash
python3 -m brain index --reindex     # Build vector index
python3 -m brain stats               # Database statistics
python3 -m brain retrieve "query"    # Retrieve documents
```

## Corpus generation (raw markdown)

| Command | Documents |
|---------|-----------|
| `make generate-smoke` | 2,000 |
| `make generate-mega` | 100,000 |
| `make generate-ultra` | 1,000,000 |
| `make generate-hyper` | Billions (uncapped) |

## Product pipeline

```bash
make product                 # Seed CHUNK corpus package
make product-premium-smoke   # Premium smoke build
make audit-distribution      # Commercial compliance check
make evaluate                # Retrieval benchmarks + evidence
```

## Configuration

| File | Purpose |
|------|---------|
| `config/product_hyper.yaml` | $1000+ premium hyper dataset |
| `config/product.yaml` | Seed corpus product build |
| `config/brain.yaml` | Brain index + retrieval |
| `config/corpus_mega.yaml` | Mega corpus generation |

## Project structure

```
.
├── brain/                  # RAG database engine
├── knowledge-base/         # Seed documents + distributable samples
├── data/product/           # Exported dataset artifacts
├── benchmarks/             # Evaluation datasets
├── scripts/
│   ├── product/            # Dataset build pipeline
│   ├── generate_corpus.py  # Corpus expansion
│   └── mega_scale.py       # Hyper-scale topic expansion
├── docs/                   # Setup, quality, licensing guides
└── examples/               # Retrieval examples
```

## License

Apache-2.0. See `LICENSE`, `NOTICE`, and `knowledge-base/PROVENANCE.md`.

Original synthetic content only — `third_party_docs_copied: false`.
