---
id: SYNAPSE-00004
title: "Synapse: auth_service ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, ci_cd_platform]
related: [HUB-AUTH_SERVICE, HUB-CI_CD_PLATFORM]
see_also: [HUB-AUTH_SERVICE, HUB-CI_CD_PLATFORM]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `auth_service` depends on `ci_cd_platform`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
