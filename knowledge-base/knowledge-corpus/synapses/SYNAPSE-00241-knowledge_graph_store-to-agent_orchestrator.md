---
id: SYNAPSE-00241
title: "Synapse: knowledge_graph_store ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, knowledge_graph_store, agent_orchestrator]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Cross-Reference Link: knowledge_graph_store → agent_orchestrator

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `knowledge_graph_store` depends on `agent_orchestrator`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
