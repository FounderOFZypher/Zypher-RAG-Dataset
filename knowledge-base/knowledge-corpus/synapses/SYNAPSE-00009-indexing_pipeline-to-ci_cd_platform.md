---
id: SYNAPSE-00009
title: "Synapse: indexing_pipeline ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, indexing_pipeline, ci_cd_platform]
related: [HUB-INDEXING_PIPELINE, HUB-CI_CD_PLATFORM]
see_also: [HUB-INDEXING_PIPELINE, HUB-CI_CD_PLATFORM]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Cross-Reference Link: indexing_pipeline → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `indexing_pipeline` is related to `ci_cd_platform`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
