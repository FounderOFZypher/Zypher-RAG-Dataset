---
id: SYNAPSE-00014
title: "Synapse: auth_service ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, incident_command]
related: [HUB-AUTH_SERVICE, HUB-INCIDENT_COMMAND]
see_also: [HUB-AUTH_SERVICE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → incident_command

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `auth_service` calls into `incident_command`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
