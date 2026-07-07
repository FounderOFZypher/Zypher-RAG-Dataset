---
id: SYNAPSE-00317
title: "Synapse: coltex_knowledge_core ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, coltex_knowledge_core, data_pipeline]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-DATA_PIPELINE]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-DATA_PIPELINE]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Cross-Reference Link: coltex_knowledge_core → data_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `coltex_knowledge_core` depends on `data_pipeline`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
