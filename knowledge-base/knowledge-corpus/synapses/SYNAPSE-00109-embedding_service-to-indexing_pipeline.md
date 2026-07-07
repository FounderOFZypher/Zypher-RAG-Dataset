---
id: SYNAPSE-00109
title: "Synapse: embedding_service ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, embedding_service, indexing_pipeline]
related: [HUB-EMBEDDING_SERVICE, HUB-INDEXING_PIPELINE]
see_also: [HUB-EMBEDDING_SERVICE, HUB-INDEXING_PIPELINE]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Cross-Reference Link: embedding_service → indexing_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `embedding_service` documents `indexing_pipeline`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
