---
id: SYNAPSE-00090
title: "Synapse: vector_store_cluster ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, vector_store_cluster, auth_service]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-AUTH_SERVICE]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-AUTH_SERVICE]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Cross-Reference Link: vector_store_cluster → auth_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `vector_store_cluster` is related to `auth_service`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
