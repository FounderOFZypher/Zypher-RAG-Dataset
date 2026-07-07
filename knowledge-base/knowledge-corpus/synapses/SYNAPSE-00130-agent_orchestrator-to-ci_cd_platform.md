---
id: SYNAPSE-00130
title: "Synapse: agent_orchestrator ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, agent_orchestrator, ci_cd_platform]
related: [HUB-AGENT_ORCHESTRATOR, HUB-CI_CD_PLATFORM]
see_also: [HUB-AGENT_ORCHESTRATOR, HUB-CI_CD_PLATFORM]
depends_on: [HUB-AGENT_ORCHESTRATOR]
---

# Cross-Reference Link: agent_orchestrator → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `agent_orchestrator` documents `ci_cd_platform`.

## Source hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
