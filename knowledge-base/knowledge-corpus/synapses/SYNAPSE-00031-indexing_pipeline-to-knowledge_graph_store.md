---
id: SYNAPSE-00031
title: "Synapse: indexing_pipeline ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, indexing_pipeline, knowledge_graph_store]
related: [HUB-INDEXING_PIPELINE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-INDEXING_PIPELINE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Cross-Reference Link: indexing_pipeline → knowledge_graph_store

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `indexing_pipeline` calls into `knowledge_graph_store`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
