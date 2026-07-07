---
id: SYNAPSE-00121
title: "Synapse: embedding_service ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, embedding_service, knowledge_graph_store]
related: [HUB-EMBEDDING_SERVICE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-EMBEDDING_SERVICE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Cross-Reference Link: embedding_service → knowledge_graph_store

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `embedding_service` documents `knowledge_graph_store`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
