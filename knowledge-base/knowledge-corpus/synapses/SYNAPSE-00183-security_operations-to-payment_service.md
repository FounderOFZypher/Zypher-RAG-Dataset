---
id: SYNAPSE-00183
title: "Synapse: security_operations ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, security_operations, payment_service]
related: [HUB-SECURITY_OPERATIONS, HUB-PAYMENT_SERVICE]
see_also: [HUB-SECURITY_OPERATIONS, HUB-PAYMENT_SERVICE]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Cross-Reference Link: security_operations → payment_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `security_operations` is related to `payment_service`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
