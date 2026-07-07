---
id: SYNAPSE-00117
title: "Synapse: embedding_service ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, embedding_service, rag_retrieval_core]
related: [HUB-EMBEDDING_SERVICE, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-EMBEDDING_SERVICE, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Cross-Reference Link: embedding_service → rag_retrieval_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `embedding_service` documents `rag_retrieval_core`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
