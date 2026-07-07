---
id: SYNAPSE-00074
title: "Synapse: ci_cd_platform ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ci_cd_platform, graphrag_engine]
related: [HUB-CI_CD_PLATFORM, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-CI_CD_PLATFORM, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Cross-Reference Link: ci_cd_platform → graphrag_engine

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `ci_cd_platform` calls into `graphrag_engine`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
