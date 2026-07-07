---
id: SYNAPSE-00293
title: "Synapse: api_gateway ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, api_gateway, vector_store_cluster]
related: [HUB-API_GATEWAY, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-API_GATEWAY, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-API_GATEWAY]
---

# Cross-Reference Link: api_gateway → vector_store_cluster

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `api_gateway` is related to `vector_store_cluster`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
