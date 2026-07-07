---
id: SYNAPSE-00260
title: "Synapse: incident_command ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, incident_command, observability_stack]
related: [HUB-INCIDENT_COMMAND, HUB-OBSERVABILITY_STACK]
see_also: [HUB-INCIDENT_COMMAND, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Cross-Reference Link: incident_command → observability_stack

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `incident_command` calls into `observability_stack`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
