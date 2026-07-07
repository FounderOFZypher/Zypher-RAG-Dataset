---
id: SYNAPSE-00238
title: "Synapse: knowledge_graph_store ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, knowledge_graph_store, ci_cd_platform]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-CI_CD_PLATFORM]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-CI_CD_PLATFORM]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Cross-Reference Link: knowledge_graph_store → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `knowledge_graph_store` is related to `ci_cd_platform`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
