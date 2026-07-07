---
id: SYNAPSE-00248
title: "Synapse: knowledge_graph_store ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, knowledge_graph_store, incident_command]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-INCIDENT_COMMAND]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Cross-Reference Link: knowledge_graph_store → incident_command

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `knowledge_graph_store` documents `incident_command`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
