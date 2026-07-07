---
id: SYNAPSE-00100
title: "Synapse: vector_store_cluster ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, vector_store_cluster, security_operations]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-SECURITY_OPERATIONS]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Cross-Reference Link: vector_store_cluster → security_operations

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `vector_store_cluster` documents `security_operations`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
