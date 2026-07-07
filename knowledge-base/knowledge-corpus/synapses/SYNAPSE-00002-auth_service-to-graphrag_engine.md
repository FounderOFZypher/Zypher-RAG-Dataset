---
id: SYNAPSE-00002
title: "Synapse: auth_service ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, graphrag_engine]
related: [HUB-AUTH_SERVICE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-AUTH_SERVICE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → graphrag_engine

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `auth_service` calls into `graphrag_engine`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
