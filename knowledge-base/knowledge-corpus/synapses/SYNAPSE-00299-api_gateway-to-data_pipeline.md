---
id: SYNAPSE-00299
title: "Synapse: api_gateway ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, api_gateway, data_pipeline]
related: [HUB-API_GATEWAY, HUB-DATA_PIPELINE]
see_also: [HUB-API_GATEWAY, HUB-DATA_PIPELINE]
depends_on: [HUB-API_GATEWAY]
---

# Cross-Reference Link: api_gateway → data_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `api_gateway` documents `data_pipeline`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
