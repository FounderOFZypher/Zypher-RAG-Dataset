---
id: SYNAPSE-00210
title: "Synapse: data_pipeline ↔ llm_inference_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, data_pipeline, llm_inference_gateway]
related: [HUB-DATA_PIPELINE, HUB-LLM_INFERENCE_GATEWAY]
see_also: [HUB-DATA_PIPELINE, HUB-LLM_INFERENCE_GATEWAY]
depends_on: [HUB-DATA_PIPELINE]
---

# Cross-Reference Link: data_pipeline → llm_inference_gateway

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `data_pipeline` documents `llm_inference_gateway`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `llm_inference_gateway`
- Anchor: `HUB-LLM_INFERENCE_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
