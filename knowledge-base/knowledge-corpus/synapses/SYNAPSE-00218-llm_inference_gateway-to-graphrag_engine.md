---
id: SYNAPSE-00218
title: "Synapse: llm_inference_gateway ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, llm_inference_gateway, graphrag_engine]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Cross-Reference Link: llm_inference_gateway → graphrag_engine

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `llm_inference_gateway` calls into `graphrag_engine`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
