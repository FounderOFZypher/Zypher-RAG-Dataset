---
id: SYNAPSE-00184
title: "Synapse: security_operations ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, security_operations, ci_cd_platform]
related: [HUB-SECURITY_OPERATIONS, HUB-CI_CD_PLATFORM]
see_also: [HUB-SECURITY_OPERATIONS, HUB-CI_CD_PLATFORM]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Cross-Reference Link: security_operations → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `security_operations` calls into `ci_cd_platform`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
