---
id: SYNAPSE-00280
title: "Synapse: ml_training_pipeline ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ml_training_pipeline, security_operations]
related: [HUB-ML_TRAINING_PIPELINE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Cross-Reference Link: ml_training_pipeline → security_operations

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `ml_training_pipeline` is related to `security_operations`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
