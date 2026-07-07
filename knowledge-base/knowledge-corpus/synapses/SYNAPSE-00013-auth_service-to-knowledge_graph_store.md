---
id: SYNAPSE-00013
title: "Synapse: auth_service ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, knowledge_graph_store]
related: [HUB-AUTH_SERVICE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-AUTH_SERVICE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → knowledge_graph_store

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `auth_service` is related to `knowledge_graph_store`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
