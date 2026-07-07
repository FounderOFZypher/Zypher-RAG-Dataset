---
id: SYNAPSE-00059
title: "Synapse: payment_service ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, payment_service, vector_store_cluster]
related: [HUB-PAYMENT_SERVICE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-PAYMENT_SERVICE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Cross-Reference Link: payment_service → vector_store_cluster

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `payment_service` depends on `vector_store_cluster`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
