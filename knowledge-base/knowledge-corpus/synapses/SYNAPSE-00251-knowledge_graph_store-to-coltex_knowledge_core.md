---
id: SYNAPSE-00251
title: "Synapse: knowledge_graph_store ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, knowledge_graph_store, coltex_knowledge_core]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Cross-Reference Link: knowledge_graph_store → coltex_knowledge_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `knowledge_graph_store` calls into `coltex_knowledge_core`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
