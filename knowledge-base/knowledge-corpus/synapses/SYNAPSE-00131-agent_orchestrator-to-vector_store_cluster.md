---
id: SYNAPSE-00131
title: "Synapse: agent_orchestrator ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, agent_orchestrator, vector_store_cluster]
related: [HUB-AGENT_ORCHESTRATOR, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Cross-Reference Link: agent_orchestrator → vector_store_cluster

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `agent_orchestrator` depends on `vector_store_cluster`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
