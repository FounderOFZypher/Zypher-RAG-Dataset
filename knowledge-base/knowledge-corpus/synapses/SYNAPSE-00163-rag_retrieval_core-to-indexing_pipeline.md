---
id: SYNAPSE-00163
title: "Synapse: rag_retrieval_core ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, rag_retrieval_core, indexing_pipeline]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-INDEXING_PIPELINE]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-INDEXING_PIPELINE]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Cross-Reference Link: rag_retrieval_core → indexing_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `rag_retrieval_core` calls into `indexing_pipeline`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
