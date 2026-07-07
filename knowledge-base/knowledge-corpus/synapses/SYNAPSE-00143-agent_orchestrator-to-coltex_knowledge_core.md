---
id: SYNAPSE-00143
title: "Synapse: agent_orchestrator ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, agent_orchestrator, coltex_knowledge_core]
related: [HUB-AGENT_ORCHESTRATOR, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Cross-Reference Link: agent_orchestrator → coltex_knowledge_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `agent_orchestrator` depends on `coltex_knowledge_core`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
