---
id: SYNAPSE-00244
title: "Synapse: knowledge_graph_store ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, knowledge_graph_store, security_operations]
related: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-KNOWLEDGE_GRAPH_STORE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-KNOWLEDGE_GRAPH_STORE]
---

# Cross-Reference Link: knowledge_graph_store → security_operations

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `knowledge_graph_store` documents `security_operations`.

## Source hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
