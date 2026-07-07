---
id: SYNAPSE-00110
title: "Synapse: embedding_service ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, embedding_service, graphrag_engine]
related: [HUB-EMBEDDING_SERVICE, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-EMBEDDING_SERVICE, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Cross-Reference Link: embedding_service → graphrag_engine

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `embedding_service` depends on `graphrag_engine`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
