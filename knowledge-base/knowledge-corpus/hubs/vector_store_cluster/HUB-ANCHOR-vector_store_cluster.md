---
id: HUB-VECTOR_STORE_CLUSTER
title: "Knowledge Cluster: Vector Store Cluster"
doc_type: architecture_decision
category: vector_stores
hub: vector_store_cluster
lobe: parietal
tags: [hub, neural-cluster, vector_store_cluster]
see_also: [CORTEX-00001]
---

# Vector Store Cluster

Central knowledge cluster for the Coltex Knowledge Corpus.

## Components
- ChromaDB
- HNSW
- pgvector
- Sharding
- Replication

## Lobe assignment
**parietal** lobe · tier `association`

## Document types in this hub
architecture_decision, benchmark, runbook, api_reference, deep_dive, troubleshooting

## GraphRAG
All documents with `hub: vector_store_cluster` form a traversable cluster.
Synapses and pathways connect this hub to other neural clusters.
