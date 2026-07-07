---
id: SYNAPSE-00106
title: "Synapse: vector_store_cluster ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, vector_store_cluster, api_gateway]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-API_GATEWAY]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-API_GATEWAY]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Cross-Reference Link: vector_store_cluster → api_gateway

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `vector_store_cluster` is related to `api_gateway`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
