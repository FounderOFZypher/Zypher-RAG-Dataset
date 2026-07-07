---
id: SYNAPSE-00126
title: "Synapse: agent_orchestrator ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, agent_orchestrator, auth_service]
related: [HUB-AGENT_ORCHESTRATOR, HUB-AUTH_SERVICE]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-AUTH_SERVICE]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Cross-Reference Link: agent_orchestrator → auth_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `agent_orchestrator` documents `auth_service`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
