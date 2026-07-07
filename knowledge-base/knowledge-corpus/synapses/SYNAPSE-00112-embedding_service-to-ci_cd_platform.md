---
id: SYNAPSE-00112
title: "Synapse: embedding_service ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, embedding_service, ci_cd_platform]
related: [HUB-EMBEDDING_SERVICE, HUB-CI_CD_PLATFORM]
see_also: [HUB-EMBEDDING_SERVICE, HUB-CI_CD_PLATFORM]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Cross-Reference Link: embedding_service → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `embedding_service` calls into `ci_cd_platform`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
