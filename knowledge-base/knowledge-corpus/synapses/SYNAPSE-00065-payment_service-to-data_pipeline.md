---
id: SYNAPSE-00065
title: "Synapse: payment_service ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, payment_service, data_pipeline]
related: [HUB-PAYMENT_SERVICE, HUB-DATA_PIPELINE]
see_also: [HUB-PAYMENT_SERVICE, HUB-DATA_PIPELINE]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Cross-Reference Link: payment_service → data_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `payment_service` calls into `data_pipeline`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
