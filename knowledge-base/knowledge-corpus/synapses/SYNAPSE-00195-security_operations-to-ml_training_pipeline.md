---
id: SYNAPSE-00195
title: "Synapse: security_operations ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, security_operations, ml_training_pipeline]
related: [HUB-SECURITY_OPERATIONS, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-SECURITY_OPERATIONS, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Cross-Reference Link: security_operations → ml_training_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `security_operations` is related to `ml_training_pipeline`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
