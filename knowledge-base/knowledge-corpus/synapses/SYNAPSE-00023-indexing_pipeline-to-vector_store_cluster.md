---
id: SYNAPSE-00023
title: "Synapse: indexing_pipeline ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, indexing_pipeline, vector_store_cluster]
related: [HUB-INDEXING_PIPELINE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-INDEXING_PIPELINE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Cross-Reference Link: indexing_pipeline → vector_store_cluster

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `indexing_pipeline` calls into `vector_store_cluster`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
