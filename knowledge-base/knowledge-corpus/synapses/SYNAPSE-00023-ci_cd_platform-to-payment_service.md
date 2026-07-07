---
id: SYNAPSE-00023
title: "Synapse: ci_cd_platform ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ci_cd_platform, payment_service]
related: [HUB-CI_CD_PLATFORM, HUB-PAYMENT_SERVICE]
see_also: [HUB-CI_CD_PLATFORM, HUB-PAYMENT_SERVICE]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Cross-Reference Link: ci_cd_platform → payment_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `ci_cd_platform` documents `payment_service`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
