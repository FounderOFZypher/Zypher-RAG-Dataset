# Zypher Product Quality Standards

The Zypher Brain product is designed for teams paying for **value, not volume**. Every build enforces quality gates defined in `config/product.yaml`.

## Core principles

### Original, well-written content

- Curated `CHUNK-*.md` documents only (no synthetic mega corpus in product builds)
- Each document has a clear title, category, and tags
- Content is structured with markdown headings for clean chunking

### Accurate metadata

Required fields on every document and chunk:

- `id` — stable document identifier
- `title` — human-readable title

Additional metadata exported in `data/product/metadata/documents.json`:

- `doc_type`, `category`, `tags`, `hub`
- Relationship counts and types
- Source path and license

### Minimal duplication

- Chunks are deduplicated by `content_hash`
- Maximum duplicate ratio: **5%** (`max_duplicate_ratio: 0.05`)
- Builds fail if duplication exceeds threshold

### Clear licensing

- All product artifacts carry `license: Apache-2.0`
- See [product-licensing.md](product-licensing.md) and root `LICENSE`

### Regular updates

- `CHANGELOG.md` tracks version history
- `data/product/manifest.json` records `built_at` timestamp and SHA-256 checksums
- `config/product.yaml` includes `version` and `updated` fields

### Documentation

- Setup guide, evaluation guide, and quality standards (this document)
- Example applications in `examples/`
- Inline docstrings in `scripts/product/`

## Quality gates

| Gate | Threshold | Enforced by |
|------|-----------|-------------|
| Min chunk size | 80 chars | `validate_quality.py` |
| Max duplicate ratio | 5% | `deduplicate.py`, `validate_quality.py` |
| Required metadata | `id`, `title` | `validate_quality.py` |
| Metadata accuracy | ≥ 90% | `evaluate_rag.py` |
| Retrieval recall@8 | ≥ 50% | `evaluate_rag.py` |
| Curated only | `true` | `config/product.yaml` |

## What we exclude from product builds

- `knowledge-base/generated/**` — procedural mega corpus
- `**/_seed/**` — internal seed copies
- Documents without `CHUNK-` prefix

## The challenge

> The biggest challenge isn't making it big — it's making it valuable.

Mega-scale generation (`make generate-hyper`) is available for stress testing, but the **product package** prioritizes:

1. Retrieval accuracy over document count
2. Graph connectivity over random volume
3. Benchmark evidence over vanity metrics
4. Checksums and manifests over undocumented dumps
