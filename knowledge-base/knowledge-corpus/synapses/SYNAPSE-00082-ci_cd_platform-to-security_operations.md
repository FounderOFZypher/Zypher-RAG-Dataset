---
id: SYNAPSE-00082
title: "Synapse: ci_cd_platform ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ci_cd_platform, security_operations]
related: [HUB-CI_CD_PLATFORM, HUB-SECURITY_OPERATIONS]
see_also: [HUB-CI_CD_PLATFORM, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Cross-Reference Link: ci_cd_platform → security_operations

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `ci_cd_platform` calls into `security_operations`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
