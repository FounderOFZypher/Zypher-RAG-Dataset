# Changelog

All notable changes to the Zypher Brain product package are documented here.

## [3.0.0] - 2026-07-06

### Removed (database-only focus)

- `zypher/` chatbot CLI and LLM provider
- `zypher_platform/` REST API, sessions, jobs, agents
- Fine-tuning scripts (`train.py`, `infer.py`, `prepare_advanced_dataset.py`)
- `config/llm.yaml`, `platform.yaml`, `zypher_xs.yaml`, `rag.yaml`
- Notebooks, Kubernetes/Docker hosting configs in knowledge-base
- Conversation memory module (chat-only)

### Changed

- Repository is now **Mega RAG Database only**
- `python3 -m brain` CLI for index / retrieve / stats
- Slimmed `requirements.txt` to RAG dependencies only

## [2.0.0] - 2026-07-06

### Added

- **$1000+ Premium RAG Dataset** — hyper-scale distributable corpus
- `mega_multiplier: 100000000000` (100 billion× tier)
- Streaming generation: `scripts/product/stream_premium_corpus.py`
- Premium content generator with 6+ sections, code examples, graph edges per document
- `make product-premium-smoke`, `make product-premium`, `make product-hyper`
- Catalog.jsonl metadata index for billion-scale document tracking
- Estimated 604+ trillion unique document combinations (procedural)

## [1.1.0] - 2026-07-06

### Added

- Commercial distribution compliance: `NOTICE`, `knowledge-base/LICENSE`, `PROVENANCE.md`
- Distribution audit (`make audit-distribution`) — scans for third-party content, forbidden markers
- Quarantined 54 non-distributable placeholder stubs to `_excluded_from_distribution/`
- `.dockerignore` excludes generated and quarantined content from releases

### Changed

- Product build excludes `_excluded_from_distribution/` from commercial package
- Documentation updated with honest content origin and licensing requirements

## [1.0.0] - 2026-07-06

### Added

- **Product pipeline** (`make product`) — curated knowledge package build
- Vector-ready chunks with accurate metadata (`data/product/chunks/`)
- Embedding generation script (`scripts/product/export_embeddings.py`)
- Graph relationship export (`data/product/graph/edges.jsonl`)
- Deduplication pipeline (max 5% duplicate ratio)
- Quality validation gates (`scripts/product/validate_quality.py`)
- Benchmark datasets: FAQ pairs, retrieval gold, RAG eval (`benchmarks/`)
- RAG evaluation with evidence report (`benchmarks/evaluation_report.json`)
- Product manifest with SHA-256 checksums (`data/product/manifest.json`)
- Curated brain config (`config/brain_curated.yaml`) — CHUNK docs only
- Example applications (`examples/rag_query.py`, `brain_retrieve.py`, `api_client.py`)
- Documentation: setup guide, quality standards, evaluation guide, licensing
- Apache-2.0 license

### Design

- Value over volume: curated `CHUNK-*.md` documents, not synthetic mega corpus
- Quality gates enforce metadata accuracy, minimal duplication, and retrieval evidence
- Brain = knowledge; LLM = reasoning engine (unchanged architecture)
