---
id: SYNAPSE-00192
title: "Synapse: security_operations ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, security_operations, llm_inference_gateway]
related: [HUB-SECURITY_OPERATIONS, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-SECURITY_OPERATIONS, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Cross-Reference Link: security_operations → llm_inference_gateway

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `security_operations` calls into `llm_inference_gateway`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
