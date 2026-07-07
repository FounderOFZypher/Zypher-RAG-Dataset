---
id: SYNAPSE-00257
title: "Synapse: incident_command ↔ vector_store_cluster"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, incident_command, vector_store_cluster]
related: [HUB-INCIDENT_COMMAND, HUB-VECTOR_STORE_CLUSTER]
see_also: [HUB-INCIDENT_COMMAND, HUB-VECTOR_STORE_CLUSTER]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Cross-Reference Link: incident_command → vector_store_cluster

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `incident_command` documents `vector_store_cluster`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
