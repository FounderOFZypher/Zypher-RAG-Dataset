---
id: SYNAPSE-00268
title: "Synapse: incident_command ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, incident_command, api_gateway]
related: [HUB-INCIDENT_COMMAND, HUB-API_GATEWAY]
see_also: [HUB-INCIDENT_COMMAND, HUB-API_GATEWAY]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Cross-Reference Link: incident_command → api_gateway

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `incident_command` calls into `api_gateway`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
