---
id: SYNAPSE-00101
title: "Synapse: vector_store_cluster ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, vector_store_cluster, data_pipeline]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-DATA_PIPELINE]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-DATA_PIPELINE]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Cross-Reference Link: vector_store_cluster → data_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `vector_store_cluster` depends on `data_pipeline`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
