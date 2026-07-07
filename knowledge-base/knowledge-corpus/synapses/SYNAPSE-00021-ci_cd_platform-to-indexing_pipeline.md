---
id: SYNAPSE-00021
title: "Synapse: ci_cd_platform ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ci_cd_platform, indexing_pipeline]
related: [HUB-CI_CD_PLATFORM, HUB-INDEXING_PIPELINE]
see_also: [HUB-CI_CD_PLATFORM, HUB-INDEXING_PIPELINE]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Cross-Reference Link: ci_cd_platform → indexing_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `ci_cd_platform` is related to `indexing_pipeline`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
