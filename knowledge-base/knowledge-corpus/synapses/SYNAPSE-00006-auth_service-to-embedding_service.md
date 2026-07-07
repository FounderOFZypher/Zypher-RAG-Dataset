---
id: SYNAPSE-00006
title: "Synapse: auth_service ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, embedding_service]
related: [HUB-AUTH_SERVICE, HUB-EMBEDDING_SERVICE]
see_also: [HUB-AUTH_SERVICE, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → embedding_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `auth_service` calls into `embedding_service`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
