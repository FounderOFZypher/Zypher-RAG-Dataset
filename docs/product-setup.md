# Coltex — Setup Guide

Build, expand, and query the Coltex enterprise knowledge corpus.

## Install

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Bootstrap the corpus

```bash
make corpus-advanced              # Full architecture bootstrap
make corpus-grow COUNT=1000       # Expand further
make corpus-mega                  # 10,000 documents
```

## Index and query

```bash
make index
python3 -m brain retrieve "How does GraphRAG work?" --context
python3 -m brain report
make corpus-report
```

## Build dataset for distribution

```bash
make product-premium-smoke
make product-premium
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
| Catalog index | `data/brain/neural-map.json` |

## Corpus generation tiers

| Command | Approximate output |
|---------|-------------------|
| `make corpus-advanced` | 500+ domain-organized docs |
| `make generate-smoke` | 2,000 documents |
| `make generate-mega` | 100,000 documents |
| `make generate-ultra` | 1,000,000 documents |

See [README](../README.md) and [architecture guide](architecture/knowledge-architecture.md).
