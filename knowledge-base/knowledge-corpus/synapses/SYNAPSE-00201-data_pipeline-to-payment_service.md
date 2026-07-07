---
id: SYNAPSE-00201
title: "Synapse: data_pipeline ↔ payment_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, data_pipeline, payment_service]
related: [HUB-DATA_PIPELINE, HUB-PAYMENT_SERVICE]
see_also: [HUB-DATA_PIPELINE, HUB-PAYMENT_SERVICE]
depends_on: [HUB-DATA_PIPELINE]
---

# Cross-Reference Link: data_pipeline → payment_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `data_pipeline` calls into `payment_service`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
