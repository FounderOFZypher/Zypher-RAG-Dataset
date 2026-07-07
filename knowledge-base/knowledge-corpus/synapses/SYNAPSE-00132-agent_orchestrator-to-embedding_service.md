---
id: SYNAPSE-00132
title: "Synapse: agent_orchestrator ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, agent_orchestrator, embedding_service]
related: [HUB-AGENT_ORCHESTRATOR, HUB-EMBEDDING_SERVICE]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Cross-Reference Link: agent_orchestrator → embedding_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `agent_orchestrator` is related to `embedding_service`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
