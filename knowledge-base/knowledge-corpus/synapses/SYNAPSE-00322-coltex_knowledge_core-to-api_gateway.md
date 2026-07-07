---
id: SYNAPSE-00322
title: "Synapse: coltex_knowledge_core ↔ api_gateway"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, coltex_knowledge_core, api_gateway]
related: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-API_GATEWAY]
see_also: [HUB-COLTEX_KNOWLEDGE_CORE, HUB-API_GATEWAY]
depends_on: [HUB-COLTEX_KNOWLEDGE_CORE]
---

# Cross-Reference Link: coltex_knowledge_core → api_gateway

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `coltex_knowledge_core` is related to `api_gateway`.

## Source hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Target hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
