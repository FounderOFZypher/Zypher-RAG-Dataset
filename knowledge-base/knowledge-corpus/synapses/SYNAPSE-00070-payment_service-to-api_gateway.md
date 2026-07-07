---
id: SYNAPSE-00070
title: "Synapse: payment_service ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, payment_service, api_gateway]
related: [HUB-PAYMENT_SERVICE, HUB-API_GATEWAY]
see_also: [HUB-PAYMENT_SERVICE, HUB-API_GATEWAY]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Cross-Reference Link: payment_service → api_gateway

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `payment_service` documents `api_gateway`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
