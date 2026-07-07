---
id: SYNAPSE-00041
title: "Synapse: graphrag_engine ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, graphrag_engine, vector_store_cluster]
related: [HUB-GRAPHRAG_ENGINE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Cross-Reference Link: graphrag_engine → vector_store_cluster

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `graphrag_engine` documents `vector_store_cluster`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
