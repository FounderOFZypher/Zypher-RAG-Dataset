---
id: SYNAPSE-00287
title: "Synapse: ml_training_pipeline ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ml_training_pipeline, coltex_knowledge_core]
related: [HUB-ML_TRAINING_PIPELINE, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Cross-Reference Link: ml_training_pipeline → coltex_knowledge_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `ml_training_pipeline` depends on `coltex_knowledge_core`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
