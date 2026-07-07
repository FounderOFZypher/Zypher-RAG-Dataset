---
id: SYNAPSE-00187
title: "Synapse: security_operations ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, security_operations, agent_orchestrator]
related: [HUB-SECURITY_OPERATIONS, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-SECURITY_OPERATIONS, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Cross-Reference Link: security_operations → agent_orchestrator

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `security_operations` is related to `agent_orchestrator`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
