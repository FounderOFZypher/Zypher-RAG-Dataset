---
id: SYNAPSE-00079
title: "Synapse: ci_cd_platform ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, ci_cd_platform, agent_orchestrator]
related: [HUB-CI_CD_PLATFORM, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-CI_CD_PLATFORM, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-CI_CD_PLATFORM]
---

# Cross-Reference Link: ci_cd_platform → agent_orchestrator

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `ci_cd_platform` documents `agent_orchestrator`.

## Source hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
