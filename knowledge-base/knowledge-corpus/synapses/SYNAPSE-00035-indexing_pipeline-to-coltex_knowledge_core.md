---
id: SYNAPSE-00035
title: "Synapse: indexing_pipeline ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, indexing_pipeline, coltex_knowledge_core]
related: [HUB-INDEXING_PIPELINE, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-INDEXING_PIPELINE, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Cross-Reference Link: indexing_pipeline → coltex_knowledge_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `indexing_pipeline` calls into `coltex_knowledge_core`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
