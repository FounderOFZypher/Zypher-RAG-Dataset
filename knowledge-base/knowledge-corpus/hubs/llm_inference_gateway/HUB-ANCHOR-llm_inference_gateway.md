---
id: HUB-LLM_INFERENCE_GATEWAY
title: "Knowledge Cluster: LLM Inference Gateway"
doc_type: architecture_decision
category: rag
hub: llm_inference_gateway
lobe: temporal
tags: [hub, neural-cluster, llm_inference_gateway]
see_also: [CORTEX-00001]
---

# LLM Inference Gateway

Central knowledge cluster for the Coltex Knowledge Corpus.

## Components
- OpenAI API
- Streaming
- Rate Limiting
- Token Budget

## Lobe assignment
**temporal** lobe · tier `executive`

## Document types in this hub
api_reference, architecture_decision, runbook, benchmark, troubleshooting

## GraphRAG
All documents with `hub: llm_inference_gateway` form a traversable cluster.
Synapses and pathways connect this hub to other neural clusters.
