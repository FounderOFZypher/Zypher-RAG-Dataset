---
id: SYNAPSE-00054
title: "Synapse: payment_service ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, payment_service, auth_service]
related: [HUB-PAYMENT_SERVICE, HUB-AUTH_SERVICE]
see_also: [HUB-PAYMENT_SERVICE, HUB-AUTH_SERVICE]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Cross-Reference Link: payment_service → auth_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `payment_service` documents `auth_service`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
