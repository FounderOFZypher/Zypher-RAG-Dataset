---
id: SYNAPSE-00275
title: "Synapse: ml_training_pipeline ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ml_training_pipeline, vector_store_cluster]
related: [HUB-ML_TRAINING_PIPELINE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Cross-Reference Link: ml_training_pipeline → vector_store_cluster

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `ml_training_pipeline` depends on `vector_store_cluster`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
