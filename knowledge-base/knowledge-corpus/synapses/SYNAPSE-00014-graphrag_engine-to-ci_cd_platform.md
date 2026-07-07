---
id: SYNAPSE-00014
title: "Synapse: graphrag_engine ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, graphrag_engine, ci_cd_platform]
related: [HUB-GRAPHRAG_ENGINE, HUB-CI_CD_PLATFORM]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-CI_CD_PLATFORM]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Cross-Reference Link: graphrag_engine → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `graphrag_engine` calls into `ci_cd_platform`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
