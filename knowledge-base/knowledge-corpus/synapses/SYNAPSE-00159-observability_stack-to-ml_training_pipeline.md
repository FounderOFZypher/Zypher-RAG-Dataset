---
id: SYNAPSE-00159
title: "Synapse: observability_stack ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, observability_stack, ml_training_pipeline]
related: [HUB-OBSERVABILITY_STACK, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-OBSERVABILITY_STACK, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Cross-Reference Link: observability_stack → ml_training_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `observability_stack` documents `ml_training_pipeline`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
