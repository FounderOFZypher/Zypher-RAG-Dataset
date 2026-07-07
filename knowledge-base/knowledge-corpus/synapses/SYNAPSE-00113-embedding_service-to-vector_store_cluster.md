---
id: SYNAPSE-00113
title: "Synapse: embedding_service ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, embedding_service, vector_store_cluster]
related: [HUB-EMBEDDING_SERVICE, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-EMBEDDING_SERVICE, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Cross-Reference Link: embedding_service → vector_store_cluster

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `embedding_service` documents `vector_store_cluster`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
