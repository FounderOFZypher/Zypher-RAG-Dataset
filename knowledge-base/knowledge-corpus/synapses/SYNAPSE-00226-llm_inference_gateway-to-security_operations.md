---
id: SYNAPSE-00226
title: "Synapse: llm_inference_gateway ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, llm_inference_gateway, security_operations]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-SECURITY_OPERATIONS]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Cross-Reference Link: llm_inference_gateway → security_operations

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `llm_inference_gateway` calls into `security_operations`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
