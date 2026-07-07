---
id: SYNAPSE-00229
title: "Synapse: llm_inference_gateway ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, llm_inference_gateway, knowledge_graph_store]
related: [HUB-LLM_INFERENCE_GATEWAY, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-LLM_INFERENCE_GATEWAY, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-LLM_INFERENCE_GATEWAY]
---

# Cross-Reference Link: llm_inference_gateway → knowledge_graph_store

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `llm_inference_gateway` is related to `knowledge_graph_store`.

## Source hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
