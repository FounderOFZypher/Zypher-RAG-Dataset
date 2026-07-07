---
id: SYNAPSE-00297
title: "Synapse: api_gateway ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, api_gateway, rag_retrieval_core]
related: [HUB-API_GATEWAY, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-API_GATEWAY, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-API_GATEWAY]
---

# Cross-Reference Link: api_gateway → rag_retrieval_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `api_gateway` is related to `rag_retrieval_core`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
