---
id: SYNAPSE-00092
title: "Synapse: vector_store_cluster ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, vector_store_cluster, graphrag_engine]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Cross-Reference Link: vector_store_cluster → graphrag_engine

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `vector_store_cluster` documents `graphrag_engine`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
