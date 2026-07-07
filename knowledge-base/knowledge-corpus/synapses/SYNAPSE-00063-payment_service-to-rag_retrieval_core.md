---
id: SYNAPSE-00063
title: "Synapse: payment_service ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, payment_service, rag_retrieval_core]
related: [HUB-PAYMENT_SERVICE, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-PAYMENT_SERVICE, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Cross-Reference Link: payment_service → rag_retrieval_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `payment_service` depends on `rag_retrieval_core`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
