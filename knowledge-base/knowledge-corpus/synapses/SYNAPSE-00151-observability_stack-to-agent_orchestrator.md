---
id: SYNAPSE-00151
title: "Synapse: observability_stack ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, observability_stack, agent_orchestrator]
related: [HUB-OBSERVABILITY_STACK, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-OBSERVABILITY_STACK, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Cross-Reference Link: observability_stack → agent_orchestrator

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `observability_stack` documents `agent_orchestrator`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
