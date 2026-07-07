---
id: SYNAPSE-00236
title: "Synapse: knowledge_graph_store ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, knowledge_graph_store, graphrag_engine]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Cross-Reference Link: knowledge_graph_store → graphrag_engine

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `knowledge_graph_store` documents `graphrag_engine`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
