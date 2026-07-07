---
id: SYNAPSE-00281
title: "Synapse: ml_training_pipeline ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ml_training_pipeline, data_pipeline]
related: [HUB-ML_TRAINING_PIPELINE, HUB-DATA_PIPELINE]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-DATA_PIPELINE]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Cross-Reference Link: ml_training_pipeline → data_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `ml_training_pipeline` calls into `data_pipeline`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
