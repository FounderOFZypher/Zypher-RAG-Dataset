---
id: SYNAPSE-00223
title: "Synapse: llm_inference_gateway ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, llm_inference_gateway, agent_orchestrator]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Cross-Reference Link: llm_inference_gateway → agent_orchestrator

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `llm_inference_gateway` documents `agent_orchestrator`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
