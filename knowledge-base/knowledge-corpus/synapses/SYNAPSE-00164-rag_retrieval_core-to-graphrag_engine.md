---
id: SYNAPSE-00164
title: "Synapse: rag_retrieval_core ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, rag_retrieval_core, graphrag_engine]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Cross-Reference Link: rag_retrieval_core → graphrag_engine

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `rag_retrieval_core` documents `graphrag_engine`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
