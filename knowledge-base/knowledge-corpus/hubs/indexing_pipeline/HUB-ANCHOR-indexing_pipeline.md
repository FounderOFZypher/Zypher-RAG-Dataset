---
id: HUB-INDEXING_PIPELINE
title: "Knowledge Cluster: Document Indexing Pipeline"
doc_type: architecture_decision
category: indexing
hub: indexing_pipeline
lobe: parietal
tags: [hub, neural-cluster, indexing_pipeline]
see_also: [CORTEX-00001]
---

# Document Indexing Pipeline

Central knowledge cluster for the Coltex Knowledge Corpus.

## Components
- Embeddings
- Vector Store
- Chunking
- HNSW
- Kafka

## Lobe assignment
**parietal** lobe · tier `association`

## Document types in this hub
api_reference, runbook, architecture_decision, code_walkthrough, troubleshooting, benchmark, design_document

## GraphRAG
All documents with `hub: indexing_pipeline` form a traversable cluster.
Synapses and pathways connect this hub to other neural clusters.
