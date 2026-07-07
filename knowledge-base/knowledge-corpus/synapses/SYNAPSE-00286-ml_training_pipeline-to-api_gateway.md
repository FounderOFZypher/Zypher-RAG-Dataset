---
id: SYNAPSE-00286
title: "Synapse: ml_training_pipeline ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ml_training_pipeline, api_gateway]
related: [HUB-ML_TRAINING_PIPELINE, HUB-API_GATEWAY]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-API_GATEWAY]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Cross-Reference Link: ml_training_pipeline → api_gateway

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `ml_training_pipeline` documents `api_gateway`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
