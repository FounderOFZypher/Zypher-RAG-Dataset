---
id: SYNAPSE-00303
title: "Synapse: api_gateway ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, api_gateway, ml_training_pipeline]
related: [HUB-API_GATEWAY, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-API_GATEWAY, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-API_GATEWAY]
---

# Cross-Reference Link: api_gateway → ml_training_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `api_gateway` documents `ml_training_pipeline`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
