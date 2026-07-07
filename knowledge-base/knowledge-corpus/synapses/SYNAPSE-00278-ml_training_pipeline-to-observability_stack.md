---
id: SYNAPSE-00278
title: "Synapse: ml_training_pipeline ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ml_training_pipeline, observability_stack]
related: [HUB-ML_TRAINING_PIPELINE, HUB-OBSERVABILITY_STACK]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Cross-Reference Link: ml_training_pipeline → observability_stack

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `ml_training_pipeline` documents `observability_stack`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
