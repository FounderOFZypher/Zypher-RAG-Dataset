---
id: SYNAPSE-00140
title: "Synapse: agent_orchestrator ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, agent_orchestrator, incident_command]
related: [HUB-AGENT_ORCHESTRATOR, HUB-INCIDENT_COMMAND]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-INCIDENT_COMMAND]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Cross-Reference Link: agent_orchestrator → incident_command

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `agent_orchestrator` is related to `incident_command`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
