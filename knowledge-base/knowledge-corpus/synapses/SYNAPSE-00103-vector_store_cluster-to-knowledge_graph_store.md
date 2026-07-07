---
id: SYNAPSE-00103
title: "Synapse: vector_store_cluster ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, vector_store_cluster, knowledge_graph_store]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Cross-Reference Link: vector_store_cluster → knowledge_graph_store

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `vector_store_cluster` calls into `knowledge_graph_store`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
