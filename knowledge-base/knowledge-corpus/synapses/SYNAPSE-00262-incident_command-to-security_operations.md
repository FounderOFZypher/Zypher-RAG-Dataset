---
id: SYNAPSE-00262
title: "Synapse: incident_command ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, incident_command, security_operations]
related: [HUB-INCIDENT_COMMAND, HUB-SECURITY_OPERATIONS]
see_also: [HUB-INCIDENT_COMMAND, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Cross-Reference Link: incident_command → security_operations

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `incident_command` depends on `security_operations`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
