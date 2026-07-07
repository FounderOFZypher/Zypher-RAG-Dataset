# Coltex SKU Matrix

License tiers and commercial packages for the Coltex RAG Vector Dataset.

---

## License tiers

| | **Personal** | **Professional** | **Enterprise** |
|---|---|--------------|------------------|
| **SKU** | `coltex-personal-v1` | `coltex-professional-v1` | `coltex-enterprise-v3` / premium |
| **Price** | **$79** one-time | **$399** one-time | **Custom quote** |
| **License** | [personal.md](../../licenses/personal.md) | [professional.md](../../licenses/professional.md) | [enterprise.md](../../licenses/enterprise.md) |
| **Use case** | Non-commercial | Commercial — one entity | Organization-wide deployment |
| **Intended users** | Students, hobbyists, researchers | Freelancers, startups, dev shops | Businesses, government, education, enterprises |
| **Build command** | `make product-personal` | `make product-professional` | `make product-enterprise` |

### Personal — $79

Non-commercial personal use. Learning, research, private projects.

### Professional — $399

Everything in Personal, **plus** commercial rights: revenue-generating apps, customer-facing integrations, business deployment. One company or legal entity.

See [licenses/professional.md](../../licenses/professional.md) for full terms.

### Enterprise — Custom Quote

Everything in Professional, **plus** organization-wide deployment, multiple users and teams, private/customer cloud (AWS, Azure, GCP, Kubernetes), on-premises deployment, and enterprise services (deployment assistance, training, priority support, volume licensing).

Enterprise RAG vector dataset packages include supplemental terms under the [Dataset EULA](../../licenses/eula.md). See commercial dataset tiers below.

---

## Enterprise dataset tiers

| | **Enterprise Curated** | **Premium Standard** | **Premium Hyper** |
|---|------------------------|----------------------|-------------------|
| **SKU** | `coltex-enterprise-v3` | `coltex-premium-v2.1` | `coltex-premium-hyper-v2.1` |
| **Price** | Contact | $1,000+ | $1,000+ (volume) |
| **Documents** | 12,993 curated | 25,000 streamed | Uncapped |
| **Domains** | 63 | 27 categories | 27+ categories |
| **Graph architecture** | Full (hubs, links, routes) | Streamed edges | Streamed edges |
| **Embeddings** | Optional | Pre-computed (500k cap) | Cluster-scale |
| **Benchmarks** | 200+ pairs | 500+ pairs | 500+ pairs |
| **Audit report** | ✅ | ✅ | ✅ |
| **Build command** | `make product-enterprise` | `make product-premium-smoke` | `make product-hyper` |
| **Best for** | Production RAG | Buyer validation | Maximum scale |

---

## Support & delivery

| Delivery method | Format |
|-----------------|--------|
| Git release tarball | `.tar.gz` with `data/product/` |
| Cloud storage | S3 / GCS signed URL |
| Hugging Face Dataset | Parquet or JSONL |

Contact: repository maintainer for licensing and delivery.
