---
id: SYNAPSE-00239
title: "Synapse: knowledge_graph_store ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, knowledge_graph_store, vector_store_cluster]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Cross-Reference Link: knowledge_graph_store → vector_store_cluster

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `knowledge_graph_store` calls into `vector_store_cluster`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
