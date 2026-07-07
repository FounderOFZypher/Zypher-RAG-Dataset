---
id: SYNAPSE-00203
title: "Synapse: data_pipeline ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, data_pipeline, vector_store_cluster]
related: [HUB-DATA_PIPELINE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-DATA_PIPELINE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-DATA_PIPELINE]
---

# Cross-Reference Link: data_pipeline → vector_store_cluster

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `data_pipeline` depends on `vector_store_cluster`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
