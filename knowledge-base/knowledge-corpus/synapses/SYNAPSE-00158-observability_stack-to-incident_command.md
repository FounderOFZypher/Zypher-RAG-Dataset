---
id: SYNAPSE-00158
title: "Synapse: observability_stack ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, observability_stack, incident_command]
related: [HUB-OBSERVABILITY_STACK, HUB-INCIDENT_COMMAND]
see_also: [HUB-OBSERVABILITY_STACK, HUB-INCIDENT_COMMAND]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Cross-Reference Link: observability_stack → incident_command

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `observability_stack` calls into `incident_command`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
