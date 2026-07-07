---
id: SYNAPSE-00212
title: "Synapse: data_pipeline ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, data_pipeline, incident_command]
related: [HUB-DATA_PIPELINE, HUB-INCIDENT_COMMAND]
see_also: [HUB-DATA_PIPELINE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-DATA_PIPELINE]
---

# Cross-Reference Link: data_pipeline → incident_command

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `data_pipeline` is related to `incident_command`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
