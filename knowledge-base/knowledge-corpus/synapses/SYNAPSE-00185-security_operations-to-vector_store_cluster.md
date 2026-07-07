---
id: SYNAPSE-00185
title: "Synapse: security_operations ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, security_operations, vector_store_cluster]
related: [HUB-SECURITY_OPERATIONS, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-SECURITY_OPERATIONS, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Cross-Reference Link: security_operations → vector_store_cluster

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `security_operations` documents `vector_store_cluster`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
