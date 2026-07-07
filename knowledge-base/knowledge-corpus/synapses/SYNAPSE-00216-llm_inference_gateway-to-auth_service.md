---
id: SYNAPSE-00216
title: "Synapse: llm_inference_gateway ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, llm_inference_gateway, auth_service]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-AUTH_SERVICE]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-AUTH_SERVICE]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Cross-Reference Link: llm_inference_gateway → auth_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `llm_inference_gateway` depends on `auth_service`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
