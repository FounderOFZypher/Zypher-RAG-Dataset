---
id: SYNAPSE-00015
title: "Synapse: auth_service ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, ml_training_pipeline]
related: [HUB-AUTH_SERVICE, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-AUTH_SERVICE, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → ml_training_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `auth_service` documents `ml_training_pipeline`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
