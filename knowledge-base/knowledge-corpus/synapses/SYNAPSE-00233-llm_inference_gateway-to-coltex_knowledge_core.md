---
id: SYNAPSE-00233
title: "Synapse: llm_inference_gateway ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, llm_inference_gateway, coltex_knowledge_core]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Cross-Reference Link: llm_inference_gateway → coltex_knowledge_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `llm_inference_gateway` is related to `coltex_knowledge_core`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
