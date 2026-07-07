---
id: SYNAPSE-00301
title: "Synapse: api_gateway ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, api_gateway, knowledge_graph_store]
related: [HUB-API_GATEWAY, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-API_GATEWAY, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-API_GATEWAY]
---

# Cross-Reference Link: api_gateway → knowledge_graph_store

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `api_gateway` is related to `knowledge_graph_store`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
