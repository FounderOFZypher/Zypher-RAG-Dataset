---
id: SYNAPSE-00200
title: "Synapse: data_pipeline ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, data_pipeline, graphrag_engine]
related: [HUB-DATA_PIPELINE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-DATA_PIPELINE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-DATA_PIPELINE]
---

# Cross-Reference Link: data_pipeline → graphrag_engine

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `data_pipeline` is related to `graphrag_engine`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
