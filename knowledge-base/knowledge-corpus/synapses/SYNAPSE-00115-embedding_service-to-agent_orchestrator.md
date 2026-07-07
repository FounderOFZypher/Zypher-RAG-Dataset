---
id: SYNAPSE-00115
title: "Synapse: embedding_service ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, embedding_service, agent_orchestrator]
related: [HUB-EMBEDDING_SERVICE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-EMBEDDING_SERVICE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Cross-Reference Link: embedding_service → agent_orchestrator

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `embedding_service` is related to `agent_orchestrator`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
