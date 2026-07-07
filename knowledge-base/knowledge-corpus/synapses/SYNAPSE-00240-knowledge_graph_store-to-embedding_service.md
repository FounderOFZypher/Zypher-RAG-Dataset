---
id: SYNAPSE-00240
title: "Synapse: knowledge_graph_store ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, knowledge_graph_store, embedding_service]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-EMBEDDING_SERVICE]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Cross-Reference Link: knowledge_graph_store → embedding_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `knowledge_graph_store` documents `embedding_service`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
