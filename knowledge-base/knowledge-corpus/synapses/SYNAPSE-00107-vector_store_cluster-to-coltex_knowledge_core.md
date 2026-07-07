---
id: SYNAPSE-00107
title: "Synapse: vector_store_cluster ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, vector_store_cluster, coltex_knowledge_core]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Cross-Reference Link: vector_store_cluster → coltex_knowledge_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `vector_store_cluster` calls into `coltex_knowledge_core`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
