---
id: SYNAPSE-00148
title: "Synapse: observability_stack ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, observability_stack, ci_cd_platform]
related: [HUB-OBSERVABILITY_STACK, HUB-CI_CD_PLATFORM]
see_also: [HUB-OBSERVABILITY_STACK, HUB-CI_CD_PLATFORM]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Cross-Reference Link: observability_stack → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `observability_stack` depends on `ci_cd_platform`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
