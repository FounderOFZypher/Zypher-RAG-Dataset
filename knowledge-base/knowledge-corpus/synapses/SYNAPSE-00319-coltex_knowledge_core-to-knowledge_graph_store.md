---
id: SYNAPSE-00319
title: "Synapse: coltex_knowledge_core ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, coltex_knowledge_core, knowledge_graph_store]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Cross-Reference Link: coltex_knowledge_core → knowledge_graph_store

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `coltex_knowledge_core` calls into `knowledge_graph_store`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
