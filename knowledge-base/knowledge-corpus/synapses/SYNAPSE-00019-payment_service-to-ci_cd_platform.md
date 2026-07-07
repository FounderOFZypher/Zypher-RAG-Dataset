---
id: SYNAPSE-00019
title: "Synapse: payment_service ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, payment_service, ci_cd_platform]
related: [HUB-PAYMENT_SERVICE, HUB-CI_CD_PLATFORM]
see_also: [HUB-PAYMENT_SERVICE, HUB-CI_CD_PLATFORM]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Cross-Reference Link: payment_service → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `payment_service` documents `ci_cd_platform`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
