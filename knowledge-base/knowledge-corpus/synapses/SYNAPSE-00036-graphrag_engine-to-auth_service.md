---
id: SYNAPSE-00036
title: "Synapse: graphrag_engine ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, graphrag_engine, auth_service]
related: [HUB-GRAPHRAG_ENGINE, HUB-AUTH_SERVICE]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-AUTH_SERVICE]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Cross-Reference Link: graphrag_engine → auth_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `graphrag_engine` calls into `auth_service`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
