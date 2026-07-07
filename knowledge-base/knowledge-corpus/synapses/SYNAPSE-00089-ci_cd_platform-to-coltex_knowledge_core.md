---
id: SYNAPSE-00089
title: "Synapse: ci_cd_platform ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ci_cd_platform, coltex_knowledge_core]
related: [HUB-CI_CD_PLATFORM, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-CI_CD_PLATFORM, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Cross-Reference Link: ci_cd_platform → coltex_knowledge_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `ci_cd_platform` is related to `coltex_knowledge_core`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
