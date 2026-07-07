---
id: SYNAPSE-00169
title: "Synapse: rag_retrieval_core ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, rag_retrieval_core, agent_orchestrator]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Cross-Reference Link: rag_retrieval_core → agent_orchestrator

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `rag_retrieval_core` depends on `agent_orchestrator`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
