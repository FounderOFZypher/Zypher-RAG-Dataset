---
id: SYNAPSE-00320
title: "Synapse: coltex_knowledge_core ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, coltex_knowledge_core, incident_command]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-INCIDENT_COMMAND]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Cross-Reference Link: coltex_knowledge_core → incident_command

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `coltex_knowledge_core` documents `incident_command`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
