---
id: SYNAPSE-00250
title: "Synapse: knowledge_graph_store ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, knowledge_graph_store, api_gateway]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-API_GATEWAY]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-API_GATEWAY]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Cross-Reference Link: knowledge_graph_store → api_gateway

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `knowledge_graph_store` is related to `api_gateway`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
