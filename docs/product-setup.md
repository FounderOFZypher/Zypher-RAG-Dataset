# Zypher Product Setup Guide

This guide walks through building the **value-first Zypher Brain product package** — curated knowledge, vector-ready chunks, embeddings, graph relationships, benchmarks, and evaluation evidence.

## What you get

| Artifact | Path | Purpose |
|----------|------|---------|
| Curated knowledge base | `knowledge-base/CHUNK-*.md` | Original synthetic docs (Apache-2.0) |
| Vector-ready chunks | `data/product/chunks/chunks.jsonl` | Chunked text + metadata |
| Embeddings | `data/product/embeddings/embeddings.jsonl` | Pre-computed vectors |
| Graph edges | `data/product/graph/edges.jsonl` | Typed relationships |
| Document metadata | `data/product/metadata/documents.json` | Accurate doc index |
| Benchmarks | `benchmarks/*.jsonl` | FAQ, retrieval gold, RAG eval |
| Evaluation report | `benchmarks/evaluation_report.json` | Evidence of AI improvement |
| Product manifest | `data/product/manifest.json` | Checksums + version |

## Prerequisites

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Quick build

```bash
# Full product pipeline with distribution compliance audit
make product

# Verify commercial distribution rights before release
make audit-distribution

# Run evaluation against curated brain
make evaluate
```

## Step-by-step

```bash
make chunks          # Build vector-ready chunks
make deduplicate     # Remove duplicate content
make validate        # Quality gate checks
make export-graph    # Export graph relationships
make embeddings      # Generate embeddings
make benchmarks      # Build benchmark datasets
make manifest             # Build product manifest
make audit-distribution   # Commercial distribution rights audit
make evaluate             # Run RAG evaluation + evidence report
```

## Curated brain mode

For production RAG, use the curated brain config (excludes synthetic generated corpus):

```bash
# Index curated documents only
BRAIN_CONFIG=config/brain_curated.yaml make index

# Or use the RAG example
python3 examples/rag_query.py "What is RAG for code?"
```

## Configuration

Edit `config/product.yaml` to adjust:

- Quality gates (`min_chunk_chars`, `max_duplicate_ratio`)
- Chunking (`max_chunk_chars`, `overlap_chars`)
- Embedding model
- Evaluation thresholds (`min_retrieval_recall`, `min_metadata_accuracy`)

## Examples

```bash
python3 examples/rag_query.py "How does GraphRAG work?"
python3 examples/brain_retrieve.py "chunking strategies"
python3 examples/api_client.py "What is RAG?"   # requires `make serve`
```

## Updating the product

1. Add or edit `knowledge-base/CHUNK-*.md` documents
2. Run `make product`
3. Review `benchmarks/evaluation_report.json`
4. Update `CHANGELOG.md`

See also: [Quality Standards](product-quality.md) · [Evaluation Guide](product-evaluation.md) · [Licensing](product-licensing.md)
