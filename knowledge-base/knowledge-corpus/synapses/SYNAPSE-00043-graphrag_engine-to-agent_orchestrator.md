---
id: SYNAPSE-00043
title: "Synapse: graphrag_engine ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, graphrag_engine, agent_orchestrator]
related: [HUB-GRAPHRAG_ENGINE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Cross-Reference Link: graphrag_engine → agent_orchestrator

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `graphrag_engine` is related to `agent_orchestrator`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
