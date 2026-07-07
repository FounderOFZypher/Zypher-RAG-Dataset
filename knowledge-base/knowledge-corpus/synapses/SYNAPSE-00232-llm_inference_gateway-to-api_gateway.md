---
id: SYNAPSE-00232
title: "Synapse: llm_inference_gateway ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, llm_inference_gateway, api_gateway]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-API_GATEWAY]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-API_GATEWAY]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Cross-Reference Link: llm_inference_gateway → api_gateway

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `llm_inference_gateway` depends on `api_gateway`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
