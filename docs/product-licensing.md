# Zypher Product Licensing

## Knowledge base content

All distributable knowledge base content is **original synthetic documentation**
authored for Zypher. It was **not** copied from third-party documentation,
web scraping, or proprietary sources.

| Content | License | Included in product? |
|---------|---------|---------------------|
| Distributable `CHUNK-*.md` files | Apache-2.0 | Yes |
| `knowledge-base/LICENSE` | Apache-2.0 | Yes |
| `knowledge-base/_excluded_from_distribution/` | Apache-2.0 | **No** — quarantined stubs |
| `knowledge-base/generated/` | Apache-2.0 | **No** — stress-test corpus only |

See `knowledge-base/PROVENANCE.md` for full content origin documentation.

## Project license

The Zypher Brain product package is released under the **Apache License 2.0**.
See the root [`LICENSE`](../LICENSE) file for the full legal text.

## NOTICE file

Third-party open-source dependencies are listed in the root [`NOTICE`](../NOTICE)
file, as required by Apache-2.0 distribution.

## What is covered

| Component | License |
|-----------|---------|
| Curated knowledge base (distributable CHUNK docs) | Apache-2.0 |
| Product artifacts (`data/product/`) | Apache-2.0 |
| Benchmark datasets (`benchmarks/`) | Apache-2.0 |
| Scripts and tooling (`scripts/product/`) | Apache-2.0 |
| Examples (`examples/`) | Apache-2.0 |

## Third-party dependencies (runtime)

These are **not bundled** in the knowledge package but are used when running
the RAG pipeline:

| Dependency | License | Notes |
|------------|---------|-------|
| sentence-transformers | Apache-2.0 | Embedding library |
| `all-MiniLM-L6-v2` model | Apache-2.0 | Downloaded from Hugging Face |
| chromadb | Apache-2.0 | Vector store |
| PyTorch | BSD-style | ML framework |
| transformers | Apache-2.0 | Model loading |
| FastAPI / uvicorn | MIT | Platform API |

## Runtime dependencies (not bundled)

| Component | License |
|-----------|---------|
| sentence-transformers | Apache-2.0 |
| `all-MiniLM-L6-v2` model | Apache-2.0 |
| chromadb | Apache-2.0 |

This package is a **RAG database only** — no LLM weights are included.

## Commercial distribution checklist

Before offering the package commercially:

```bash
make product              # Build with compliance gates
make audit-distribution   # Verify distribution rights
```

The audit checks for:

- Required `LICENSE`, `NOTICE`, and `PROVENANCE.md` files
- No excluded paths in product artifacts
- No forbidden third-party source patterns in content
- No placeholder boilerplate in distributable documents

## Usage rights

You may:

- Use the product package in commercial applications
- Modify and redistribute under Apache-2.0 terms
- Build derivative datasets with attribution

You must:

- Include the Apache-2.0 license notice and `NOTICE` file
- State significant changes in derivative works
- Not use Zypher trademarks without permission
- Not redistribute quarantined or generated corpus as curated knowledge

## Disclaimer

This document describes the project's licensing approach. It is not legal advice.
Consult qualified counsel before commercial distribution.
