---
id: SYNAPSE-00098
title: "Synapse: vector_store_cluster ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, vector_store_cluster, observability_stack]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-OBSERVABILITY_STACK]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Cross-Reference Link: vector_store_cluster → observability_stack

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `vector_store_cluster` is related to `observability_stack`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
