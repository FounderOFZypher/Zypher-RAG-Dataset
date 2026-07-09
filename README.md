# Coltex

**Commercial RAG corpus — 100,000,000+ documents for production retrieval systems.**

Coltex Mega RAG is a GraphRAG-ready knowledge corpus: streaming-generated, embedding-ready,
and packaged for commercial distribution as domain packs and the full Mega SKU.

---

## Deliverables

| Artifact | Description |
|----------|-------------|
| **Document corpus** | 100,000,000+ original synthetic knowledge documents |
| **Vector chunks** | Metadata-rich JSONL for vector stores |
| **Knowledge graph** | Typed edges for GraphRAG routing |
| **Marketplace packs** | Domain packs (RAG, languages, cloud, security, architecture) |
| **Benchmarks** | FAQ pairs, retrieval gold sets, RAG evaluation sets |
| **Compliance** | Provenance, EULA, distribution audit |

Commercial packaging: [docs/commercial/product-overview.md](docs/commercial/product-overview.md) · [SKU matrix](docs/commercial/sku-matrix.md)

---

## Quick start

```bash
git clone https://github.com/FounderOfColtex/Coltex-Knowledge-Platform.git
cd Coltex-Knowledge-Platform
python -m venv .venv
source .venv/bin/activate
pip install -e .

# Validate the Mega commercial pipeline (capped build)
make product-mega-smoke

# Inspect artifacts
python3 examples/load_dataset.py
make audit-distribution
```

Full Mega build (cluster — uncapped 100M+):

```bash
make product-mega
```

---

## Commercial SKUs

| SKU | Scale | License |
|-----|-------|---------|
| Personal | Sample pack (~25k) | Personal + EULA |
| Professional | Domain packs (1M–10M) | Professional + EULA |
| Enterprise | Multi-domain (10M–50M) | Enterprise + EULA |
| **Mega** | **100,000,000+** | Mega + EULA |

Licenses: [EULA.md](EULA.md) · [MEGA-LICENSE.md](MEGA-LICENSE.md) · [PERSONAL-LICENSE.md](PERSONAL-LICENSE.md) · [PROFESSIONAL-LICENSE.md](PROFESSIONAL-LICENSE.md) · [ENTERPRISE-LICENSE.md](ENTERPRISE-LICENSE.md)

Runtime source remains **MIT** ([LICENSE](LICENSE)).

---

## Marketplace packs

Available individually or bundled — see [config/marketplace.yaml](config/marketplace.yaml):

- `pack-rag-core` — RAG, GraphRAG, embeddings, retrieval
- `pack-languages` — Python, JS/TS, Go, Rust, Java, C#, SQL
- `pack-cloud-devops` — AWS, Azure, GCP, Kubernetes, Terraform, CI/CD
- `pack-security-sre` — Security, observability, incidents
- `pack-architecture` — Microservices, DDD, APIs, data stores

```bash
make marketplace-packs
```

---

## Runtime

```bash
coltex serve                  # web console — http://<server-ip>:8080
coltex deploy                 # show access URLs
```

| Profile | Bind | Port |
|---------|------|------|
| `lan` | 0.0.0.0 | 8080 |
| `production` | 0.0.0.0 | 443 |

Docker: `docker compose up -d` — guide: [docs/deployment/self-hosted.md](docs/deployment/self-hosted.md)

| Profile | Bind | Port |
|---------|------|------|
| `lan` | 0.0.0.0 | 8080 |
| `production` | 0.0.0.0 | 443 |

## Capabilities

1. **Streaming generation** — memory-safe corpus builds at Mega scale
2. **GraphRAG-native** — hubs and typed relationships on every document
3. **Hybrid retrieval** — dense vectors with metadata filters
4. **Quality gates** — substance checks, duplicate caps, commercial audit
5. **Commercial packaging** — SKUs, packs, catalog, and EULA
6. **Evaluation harness** — recall@k and metadata accuracy benchmarks

---

## Documentation

| Doc | Purpose |
|-----|---------|
| [Commercial overview](docs/commercial/product-overview.md) | Product packaging |
| [Datasheet](docs/commercial/datasheet.md) | Technical specification |
| [SKU matrix](docs/commercial/sku-matrix.md) | SKUs and packs |
| [Platform overview](docs/platform/overview.md) | Runtime architecture |
| [Product setup](docs/product-setup.md) | Build and query |

---

## License

- **Runtime:** MIT — [LICENSE](LICENSE)
- **Commercial Mega RAG dataset:** [EULA.md](EULA.md)
