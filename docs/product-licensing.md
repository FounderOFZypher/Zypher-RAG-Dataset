# Zypher Product Licensing

## License

The Zypher Brain product package is released under the **Apache License 2.0**.

See the root [`LICENSE`](../LICENSE) file for the full legal text.

## What is covered

| Component | License |
|-----------|---------|
| Curated knowledge base (`knowledge-base/CHUNK-*.md`) | Apache-2.0 |
| Product artifacts (`data/product/`) | Apache-2.0 |
| Benchmark datasets (`benchmarks/`) | Apache-2.0 |
| Scripts and tooling (`scripts/product/`) | Apache-2.0 |
| Examples (`examples/`) | Apache-2.0 |

## Third-party dependencies

| Dependency | License |
|------------|---------|
| sentence-transformers | Apache-2.0 |
| chromadb | Apache-2.0 |
| PyTorch | BSD-style |
| transformers | Apache-2.0 |

Embedding model `sentence-transformers/all-MiniLM-L6-v2` is subject to its own model card terms on Hugging Face.

## Usage rights

You may:

- Use the product package in commercial applications
- Modify and redistribute under Apache-2.0 terms
- Build derivative datasets with attribution

You must:

- Include the Apache-2.0 license notice
- State significant changes in derivative works
- Not use Zypher trademarks without permission

## Product manifest

Each build records the license in:

- `config/product.yaml` → `license: Apache-2.0`
- `data/product/manifest.json` → `"license": "Apache-2.0"`
- Per-chunk metadata → `"license": "Apache-2.0"`

## Questions

For enterprise licensing inquiries, contact your Zypher account representative.
