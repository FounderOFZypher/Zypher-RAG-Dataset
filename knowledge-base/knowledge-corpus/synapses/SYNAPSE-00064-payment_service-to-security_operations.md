---
id: SYNAPSE-00064
title: "Synapse: payment_service ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, payment_service, security_operations]
related: [HUB-PAYMENT_SERVICE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-PAYMENT_SERVICE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Cross-Reference Link: payment_service → security_operations

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `payment_service` is related to `security_operations`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
