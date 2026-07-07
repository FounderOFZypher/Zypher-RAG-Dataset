---
id: SYNAPSE-00067
title: "Synapse: payment_service ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, payment_service, knowledge_graph_store]
related: [HUB-PAYMENT_SERVICE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-PAYMENT_SERVICE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Cross-Reference Link: payment_service → knowledge_graph_store

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `payment_service` depends on `knowledge_graph_store`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
