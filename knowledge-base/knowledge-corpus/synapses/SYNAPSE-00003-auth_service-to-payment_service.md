---
id: SYNAPSE-00003
title: "Synapse: auth_service ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, payment_service]
related: [HUB-AUTH_SERVICE, HUB-PAYMENT_SERVICE]
see_also: [HUB-AUTH_SERVICE, HUB-PAYMENT_SERVICE]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → payment_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `auth_service` documents `payment_service`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
