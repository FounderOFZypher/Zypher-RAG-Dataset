---
id: SYNAPSE-00256
title: "Synapse: incident_command ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, incident_command, ci_cd_platform]
related: [HUB-INCIDENT_COMMAND, HUB-CI_CD_PLATFORM]
see_also: [HUB-INCIDENT_COMMAND, HUB-CI_CD_PLATFORM]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Cross-Reference Link: incident_command → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `incident_command` calls into `ci_cd_platform`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
