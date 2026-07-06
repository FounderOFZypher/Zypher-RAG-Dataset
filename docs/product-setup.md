# Zypher Mega RAG Database — Setup Guide

Build and export the premium RAG dataset artifacts.

## Install

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Build dataset

```bash
# Premium smoke (10,000 documents)
make product-premium-smoke

# Full hyper tier (100B× — run on cluster)
make product-hyper

# Compliance audit
make audit-distribution
```

## Output artifacts

| Artifact | Path |
|----------|------|
| Chunks | `data/product/chunks/chunks.jsonl` |
| Catalog | `data/product/catalog.jsonl` |
| Embeddings | `data/product/embeddings/embeddings.jsonl` |
| Graph | `data/product/graph/edges.jsonl` |
| Manifest | `data/product/manifest.json` |

## Query the database

```bash
make index
python3 -m brain retrieve "How does GraphRAG work?" --context
python3 examples/rag_query.py "chunking strategies"
python3 examples/brain_retrieve.py "RAG principles"
```

## Configuration

- `config/product_hyper.yaml` — $1000+ premium hyper dataset
- `config/product_hyper_smoke.yaml` — local smoke test
- `config/brain.yaml` — vector index + retrieval

See also: [Quality Standards](product-quality.md) · [Licensing](product-licensing.md) · [Evaluation](product-evaluation.md)
