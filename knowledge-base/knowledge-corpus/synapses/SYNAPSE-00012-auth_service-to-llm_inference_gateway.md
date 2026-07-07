---
id: SYNAPSE-00012
title: "Synapse: auth_service ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, llm_inference_gateway]
related: [HUB-AUTH_SERVICE, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-AUTH_SERVICE, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → llm_inference_gateway

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `auth_service` depends on `llm_inference_gateway`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
