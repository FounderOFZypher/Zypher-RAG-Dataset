---
id: SYNAPSE-00049
title: "Synapse: graphrag_engine ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, graphrag_engine, knowledge_graph_store]
related: [HUB-GRAPHRAG_ENGINE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Cross-Reference Link: graphrag_engine → knowledge_graph_store

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `graphrag_engine` documents `knowledge_graph_store`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
