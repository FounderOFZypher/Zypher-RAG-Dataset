# Coltex Advanced Retrieval

Coltex Mega RAG ships a production hybrid retrieval stack with mode routing,
cross-encoder reranking, context compression, incremental indexing, multi-workspace
federation, and a wired plugin system.

---

## Capabilities

| Capability | Status | Notes |
|------------|--------|-------|
| Vector RAG | Available | Chroma + bi-encoder dense retrieval |
| GraphRAG | Available | Multi-hop graph expansion + region routing |
| Hybrid Retrieval | Available | Dense + sparse + metadata + graph fusion |
| BM25 Search | Available | Okapi BM25 lexical index |
| Metadata Search | Available | doc_type / hub / category / tag scoring |
| SQL Retrieval | Available | Schema / SQL example / migration scoped search |
| Code Retrieval | Available | Code walkthrough + identifier boosting |
| API Retrieval | Available | HTTP method / path / OpenAPI-aware search |
| Multi-Vector Retrieval | Available | Title + body + code role embeddings |
| Cross-Encoder Reranking | Available | Neural CE with lexical fallback |
| Context Compression | Available | Extractive sentence compression |
| Context Builder | Available | Ranked blocks, diversity, attribution |
| Explainable Retrieval | Available | Per-hit factor breakdown + trace |
| Incremental Indexing | Available | Upsert / delete across backends |
| Multi-workspace | Available | Federated `.ctex` search |
| Plugin System | Available | Search algorithms + pre/post retrieve hooks |

### Extra advanced features

- Query expansion (deterministic synonym map)
- Parent-document / hub expansion
- Freshness boosting
- Reciprocal Rank Fusion (`--mode rrf`)
- Metadata filters (`--doc-type`, `--category`)

---

## Modes

```bash
coltex search "JWT authentication" --mode hybrid
coltex search "SELECT join index" --mode sql
coltex search "refactor AuthService" --mode code
coltex search "GET /v1/payments" --mode api
coltex search "vector store failover" --mode graphrag
coltex search "chunk overlap" --mode bm25
coltex search "rag evaluation" --mode multi_vector --explain
coltex capabilities
coltex federated-search "incident runbook" --workspace ./TeamA.ctex --workspace ./TeamB.ctex
```

---

## Pipeline

```
Query
  → expand
  → Vector · BM25 · Metadata · Multi-Vector · SQL · Code · API · Plugins
  → GraphRAG expansion
  → Weighted fusion or RRF
  → Parent docs + freshness
  → Cross-encoder rerank
  → Context compress + build
  → Explainable result + trace
```

Config: `config/brain.yaml` → `retrieval.advanced`

---

## Plugins

```python
from runtime.plugins import sdk

def my_search(query: str, mode: str = "hybrid", brain_pipeline=None):
    # return list[ScoredDocument]
    return []

sdk.register_search_algorithm("domain_router", my_search)
sdk.subscribe_event("pre_retrieve", lambda **kw: None)
sdk.subscribe_event("post_retrieve", lambda **kw: None)
```

---

## Incremental indexing

```python
brain.index_document(doc)   # upsert across vector / multi-vector / BM25 / specialized
brain.delete_document(doc_id)
```
