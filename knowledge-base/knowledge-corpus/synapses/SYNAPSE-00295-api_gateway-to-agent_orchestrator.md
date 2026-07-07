---
id: SYNAPSE-00295
title: "Synapse: api_gateway ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, api_gateway, agent_orchestrator]
related: [HUB-API_GATEWAY, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-API_GATEWAY, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-API_GATEWAY]
---

# Cross-Reference Link: api_gateway → agent_orchestrator

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `api_gateway` documents `agent_orchestrator`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
