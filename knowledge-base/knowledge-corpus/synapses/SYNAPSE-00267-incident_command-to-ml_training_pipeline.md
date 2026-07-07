---
id: SYNAPSE-00267
title: "Synapse: incident_command ↔ ml_training_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, incident_command, ml_training_pipeline]
related: [HUB-INCIDENT_COMMAND, HUB-ML_TRAINING_PIPELINE]
see_also: [HUB-INCIDENT_COMMAND, HUB-ML_TRAINING_PIPELINE]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Cross-Reference Link: incident_command → ml_training_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `incident_command` is related to `ml_training_pipeline`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `ml_training_pipeline`
- Anchor: `HUB-ML_TRAINING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
