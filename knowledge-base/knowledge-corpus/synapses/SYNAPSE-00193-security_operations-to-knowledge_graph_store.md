---
id: SYNAPSE-00193
title: "Synapse: security_operations ↔ knowledge_graph_store"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, security_operations, knowledge_graph_store]
related: [HUB-SECURITY_OPERATIONS, HUB-KNOWLEDGE_GRAPH_STORE]
see_also: [HUB-SECURITY_OPERATIONS, HUB-KNOWLEDGE_GRAPH_STORE]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Cross-Reference Link: security_operations → knowledge_graph_store

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `security_operations` documents `knowledge_graph_store`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `knowledge_graph_store`
- Anchor: `HUB-KNOWLEDGE_GRAPH_STORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
