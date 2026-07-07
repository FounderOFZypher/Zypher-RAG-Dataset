---
id: SYNAPSE-00052
title: "Synapse: graphrag_engine ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, graphrag_engine, api_gateway]
related: [HUB-GRAPHRAG_ENGINE, HUB-API_GATEWAY]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-API_GATEWAY]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Cross-Reference Link: graphrag_engine → api_gateway

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `graphrag_engine` calls into `api_gateway`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
