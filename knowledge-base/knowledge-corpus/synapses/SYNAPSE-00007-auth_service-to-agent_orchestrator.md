---
id: SYNAPSE-00007
title: "Synapse: auth_service ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, agent_orchestrator]
related: [HUB-AUTH_SERVICE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-AUTH_SERVICE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → agent_orchestrator

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `auth_service` documents `agent_orchestrator`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
