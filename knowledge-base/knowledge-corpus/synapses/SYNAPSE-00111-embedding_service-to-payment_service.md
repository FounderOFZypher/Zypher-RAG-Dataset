---
id: SYNAPSE-00111
title: "Synapse: embedding_service ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, embedding_service, payment_service]
related: [HUB-EMBEDDING_SERVICE, HUB-PAYMENT_SERVICE]
see_also: [HUB-EMBEDDING_SERVICE, HUB-PAYMENT_SERVICE]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Cross-Reference Link: embedding_service → payment_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `embedding_service` is related to `payment_service`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
