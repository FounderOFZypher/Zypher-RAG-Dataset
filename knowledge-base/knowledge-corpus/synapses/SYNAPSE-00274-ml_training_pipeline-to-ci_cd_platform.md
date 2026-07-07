---
id: SYNAPSE-00274
title: "Synapse: ml_training_pipeline ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ml_training_pipeline, ci_cd_platform]
related: [HUB-ML_TRAINING_PIPELINE, HUB-CI_CD_PLATFORM]
see_also: [HUB-ML_TRAINING_PIPELINE, HUB-CI_CD_PLATFORM]
depends_on: [HUB-ML_TRAINING_PIPELINE]
---

# Cross-Reference Link: ml_training_pipeline → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `ml_training_pipeline` documents `ci_cd_platform`.

## Source hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
