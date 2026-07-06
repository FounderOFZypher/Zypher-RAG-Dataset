# Knowledge Base Provenance

This document records the origin of content in the Zypher Brain knowledge base for
commercial distribution compliance.

## Content origin

| Category | Origin | Third-party sources |
|----------|--------|---------------------|
| FAQ documents (`CHUNK-00000`–`00004`) | Originally authored for Zypher | None |
| Graph relationship nodes | Synthetically generated fictional architecture | None |
| Architecture decision records (ADRs) | Synthetically generated | None |
| Incident reports & runbooks | Synthetically generated | None |
| Code review examples | Original minimal Python examples | None |
| OpenAPI / Kubernetes / SQL configs | Original minimal stubs | None |

## What is NOT included in commercial distribution

| Path | Reason |
|------|--------|
| `knowledge-base/_excluded_from_distribution/` | Placeholder stubs — insufficient substance for distribution |
| `knowledge-base/generated/` | Procedural mega-corpus for stress testing only |
| `knowledge-base/_seed/` | Internal seed copies |

## Generation method

- **No web scraping** of third-party documentation
- **No copying** from HuggingFace, LangChain, Kubernetes, Python, or other official docs
- **No LLM API generation** from external sources in the corpus pipeline
- Corpus expansion scripts (`scripts/generate_corpus.py`) use in-repo string templates only

## Technology references

Documents may reference technologies by name (e.g., Kafka, Kubernetes, tree-sitter,
ChromaDB) in descriptive context. These are **nominative references**, not reproduced
documentation from those projects.

## Runtime dependencies (not bundled)

The following are downloaded at runtime and subject to their own licenses:

| Component | License | Notes |
|-----------|---------|-------|
| `sentence-transformers/all-MiniLM-L6-v2` | Apache-2.0 | Embedding model |
| `poolside/Laguna-XS-2.1` | Custom HF license | LLM — accept terms on Hugging Face before use |
| PyTorch, transformers, chromadb | Various open source | See root `NOTICE` |

## Verification

Run the distribution audit before any commercial release:

```bash
make audit-distribution
```
