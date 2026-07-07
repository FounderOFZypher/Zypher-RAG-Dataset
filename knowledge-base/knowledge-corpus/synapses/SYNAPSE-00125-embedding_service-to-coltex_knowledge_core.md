---
id: SYNAPSE-00125
title: "Synapse: embedding_service ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, embedding_service, coltex_knowledge_core]
related: [HUB-EMBEDDING_SERVICE, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-EMBEDDING_SERVICE, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Cross-Reference Link: embedding_service → coltex_knowledge_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `embedding_service` documents `coltex_knowledge_core`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
