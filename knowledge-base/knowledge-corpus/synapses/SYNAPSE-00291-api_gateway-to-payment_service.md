---
id: SYNAPSE-00291
title: "Synapse: api_gateway ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, api_gateway, payment_service]
related: [HUB-API_GATEWAY, HUB-PAYMENT_SERVICE]
see_also: [HUB-API_GATEWAY, HUB-PAYMENT_SERVICE]
depends_on: [HUB-API_GATEWAY]
---

# Cross-Reference Link: api_gateway → payment_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `api_gateway` documents `payment_service`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
