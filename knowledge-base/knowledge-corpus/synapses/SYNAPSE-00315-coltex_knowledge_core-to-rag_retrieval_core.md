---
id: SYNAPSE-00315
title: "Synapse: coltex_knowledge_core ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, coltex_knowledge_core, rag_retrieval_core]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Cross-Reference Link: coltex_knowledge_core → rag_retrieval_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `coltex_knowledge_core` calls into `rag_retrieval_core`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
