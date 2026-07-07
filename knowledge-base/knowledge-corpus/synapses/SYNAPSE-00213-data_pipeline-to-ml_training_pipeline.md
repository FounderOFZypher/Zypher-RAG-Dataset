---
id: SYNAPSE-00213
title: "Synapse: data_pipeline ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, data_pipeline, ml_training_pipeline]
related: [HUB-DATA_PIPELINE, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-DATA_PIPELINE, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-DATA_PIPELINE]
---

# Cross-Reference Link: data_pipeline → ml_training_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `data_pipeline` calls into `ml_training_pipeline`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
