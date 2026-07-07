---
id: SYNAPSE-00005
title: "Synapse: auth_service ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, vector_store_cluster]
related: [HUB-AUTH_SERVICE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-AUTH_SERVICE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → vector_store_cluster

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `auth_service` is related to `vector_store_cluster`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
