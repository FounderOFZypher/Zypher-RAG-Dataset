---
id: SYNAPSE-00211
title: "Synapse: data_pipeline ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, data_pipeline, knowledge_graph_store]
related: [HUB-DATA_PIPELINE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-DATA_PIPELINE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-DATA_PIPELINE]
---

# Cross-Reference Link: data_pipeline → knowledge_graph_store

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `data_pipeline` depends on `knowledge_graph_store`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
