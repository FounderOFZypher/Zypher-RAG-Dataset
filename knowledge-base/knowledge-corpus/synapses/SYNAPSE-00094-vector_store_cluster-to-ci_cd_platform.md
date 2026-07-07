---
id: SYNAPSE-00094
title: "Synapse: vector_store_cluster ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, vector_store_cluster, ci_cd_platform]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-CI_CD_PLATFORM]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-CI_CD_PLATFORM]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Cross-Reference Link: vector_store_cluster → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `vector_store_cluster` is related to `ci_cd_platform`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
