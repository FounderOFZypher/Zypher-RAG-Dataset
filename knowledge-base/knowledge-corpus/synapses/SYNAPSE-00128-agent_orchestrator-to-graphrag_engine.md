---
id: SYNAPSE-00128
title: "Synapse: agent_orchestrator ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, agent_orchestrator, graphrag_engine]
related: [HUB-AGENT_ORCHESTRATOR, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Cross-Reference Link: agent_orchestrator → graphrag_engine

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `agent_orchestrator` is related to `graphrag_engine`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
