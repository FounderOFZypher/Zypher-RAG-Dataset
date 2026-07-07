---
id: SYNAPSE-00020
title: "Synapse: indexing_pipeline ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, indexing_pipeline, graphrag_engine]
related: [HUB-INDEXING_PIPELINE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-INDEXING_PIPELINE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Cross-Reference Link: indexing_pipeline → graphrag_engine

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `indexing_pipeline` documents `graphrag_engine`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
