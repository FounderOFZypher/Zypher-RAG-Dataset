---
id: SYNAPSE-00289
title: "Synapse: api_gateway ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, api_gateway, indexing_pipeline]
related: [HUB-API_GATEWAY, HUB-INDEXING_PIPELINE]
see_also: [HUB-API_GATEWAY, HUB-INDEXING_PIPELINE]
depends_on: [HUB-API_GATEWAY]
---

# Cross-Reference Link: api_gateway → indexing_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `api_gateway` is related to `indexing_pipeline`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
