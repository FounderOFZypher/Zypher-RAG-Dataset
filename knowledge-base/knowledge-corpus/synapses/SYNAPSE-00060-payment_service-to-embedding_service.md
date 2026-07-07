---
id: SYNAPSE-00060
title: "Synapse: payment_service ↔ embedding_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, payment_service, embedding_service]
related: [HUB-PAYMENT_SERVICE, HUB-EMBEDDING_SERVICE]
see_also: [HUB-PAYMENT_SERVICE, HUB-EMBEDDING_SERVICE]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Cross-Reference Link: payment_service → embedding_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `payment_service` is related to `embedding_service`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
