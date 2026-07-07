---
id: SYNAPSE-00104
title: "Synapse: vector_store_cluster ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, vector_store_cluster, incident_command]
related: [HUB-VECTOR_STORE_CLUSTER, HUB-INCIDENT_COMMAND]
see_also: [HUB-VECTOR_STORE_CLUSTER, HUB-INCIDENT_COMMAND]
depends_on: [HUB-VECTOR_STORE_CLUSTER]
---

# Cross-Reference Link: vector_store_cluster → incident_command

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `vector_store_cluster` documents `incident_command`.

## Source hub
- Hub: `vector_store_cluster`
- Anchor: `HUB-VECTOR_STORE_CLUSTER`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
