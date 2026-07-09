# Coltex Mega RAG — Product Overview

**Tagline:** The largest commercial RAG corpus — 100,000,000+ sellable knowledge files.

Coltex is rebuilt as a **commercial mega-scale RAG product**: a streaming-generated,
graph-linked, embedding-ready knowledge corpus designed to power production retrieval
systems — and to be sold as industry packs, shards, and full Mega SKUs.

---

## What you are buying

| Deliverable | Description |
|-------------|-------------|
| **Document corpus** | 100,000,000+ original synthetic knowledge files across 50+ domains |
| **Vector chunks** | Chunked, metadata-rich JSONL ready for embedding stores |
| **Knowledge graph** | Typed edges (see_also, depends_on, routes_to) for GraphRAG |
| **Catalog** | Machine-readable inventory for marketplace and shard sales |
| **Benchmarks** | FAQ pairs, retrieval gold, RAG eval sets |
| **Provenance + audit** | Distribution compliance artifacts for enterprise buyers |

---

## Why it is advanced

1. **Hyper-scale streaming** — procedural generation never loads the full corpus into memory
2. **GraphRAG-native** — every document ships with hub routing and relationship edges
3. **Hybrid retrieval ready** — metadata fields (doc_type, category, hub, tags) for dense + sparse search
4. **Quality gates** — substantive-content checks, duplicate caps, license/provenance audit
5. **Sellable shards** — marketplace packs by domain, industry, and document type
6. **Evaluation harness** — recall@k and metadata accuracy benchmarks included

---

## Buyers

| Segment | Use case |
|---------|----------|
| AI / ML teams | Production RAG bootstrap with a large, structured corpus |
| Platform vendors | Licensed shards in vertical AI products |
| Enterprises | Private RAG over engineering, cloud, security, and operations knowledge |
| Data marketplaces | Licensed industry packs under Coltex EULA terms |
| Researchers | Large-scale retrieval and GraphRAG evaluation |

---

## Build and inspect

```bash
# Capped validation build
make product-mega-smoke

# Full Mega commercial target (cluster)
make product-mega

# Inspect artifacts
python3 examples/load_dataset.py
make audit-distribution
```

---

## Related docs

- [SKU matrix](sku-matrix.md)
- [Datasheet](datasheet.md)
- [EULA](../../EULA.md)
- [Marketplace](../../config/marketplace.yaml)
