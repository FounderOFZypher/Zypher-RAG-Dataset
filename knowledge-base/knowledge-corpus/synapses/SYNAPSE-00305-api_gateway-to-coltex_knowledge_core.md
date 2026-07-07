---
id: SYNAPSE-00305
title: "Synapse: api_gateway ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, api_gateway, coltex_knowledge_core]
related: [HUB-API_GATEWAY, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-API_GATEWAY, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-API_GATEWAY]
---

# Cross-Reference Link: api_gateway → coltex_knowledge_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `api_gateway` is related to `coltex_knowledge_core`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
