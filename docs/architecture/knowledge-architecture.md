# Coltex Knowledge Architecture — Reference

Enterprise multi-layer RAG knowledge corpus with graph-linked domains, knowledge clusters, and advanced GraphRAG routing.

## System overview

```mermaid
flowchart TB
    subgraph layers [Processing Layers L1-L6]
        L1[L1 Ingestion]
        L2[L2 Association]
        L3[L3 Integration]
        L4[L4 Reasoning]
        L5[L5 Executive]
        L6[L6 Meta]
        L1 --> L2 --> L3 --> L4 --> L5 --> L6
    end

    subgraph clusters [Functional Clusters]
        F[Architecture]
        T[Retrieval]
        P[Data]
        O[Operations]
        L[Security]
    end

    subgraph graph [Graph Layer]
        Domains[62+ Domains]
        Hubs[18 Knowledge Hubs]
        Links[Graph Links]
        Path[Pathways]
    end

    layers --> clusters
    clusters --> graph
    graph --> Retrieve[Hybrid Retrieval]
```

## Directory layout

```
knowledge-corpus/
├── cortex/L1-sensory … L6-meta    # Processing layers
├── lobes/                           # Functional clusters
├── domains/                         # Technology categories
├── hubs/                            # Knowledge clusters
├── synapses/                        # Hub-to-hub graph links
├── pathways/                        # Inter-cluster routes
├── memory/working|episodic|…        # Retention tiers
└── reflexes/                        # Quick-reference FAQs
```

## Knowledge hubs (18)

`auth_service`, `indexing_pipeline`, `graphrag_engine`, `vector_store_cluster`, `embedding_service`, `agent_orchestrator`, `observability_stack`, `rag_retrieval_core`, `security_operations`, `data_pipeline`, `llm_inference_gateway`, `knowledge_graph_store`, `incident_command`, `ml_training_pipeline`, `api_gateway`, `payment_service`, `ci_cd_platform`, `coltex_knowledge_core`

## Graph edge types (20)

Core: `related`, `depends_on`, `uses`, `implements`, `calls`, `see_also`

Advanced: `extends`, `validates`, `synthesizes`, `triggers`, `derived_from`, `tested_by`, `deployed_via`, and more.

## GraphRouter

Region-aware graph expansion in `brain/graph/neural_router.py`:

- Graph links and pathways receive retrieval score boosts
- 4-hop traversal, 16 max expanded documents
- Enabled via `config/brain.yaml` → `graph.advanced_routing: true`

## Manifests

| File | Purpose |
|------|---------|
| `data/brain/neural-map.json` | Catalog index with per-region counts |
| `data/brain/architecture-manifest.json` | Architecture registry |
| `config/brain_architecture.yaml` | Master architecture specification |

## Commands

```bash
make corpus-advanced
make index
python3 -m brain report
python3 -m brain retrieve "your query" --context
```
