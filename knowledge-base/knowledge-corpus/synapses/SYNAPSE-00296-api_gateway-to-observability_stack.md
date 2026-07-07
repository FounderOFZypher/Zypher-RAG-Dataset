---
id: SYNAPSE-00296
title: "Synapse: api_gateway ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, api_gateway, observability_stack]
related: [HUB-API_GATEWAY, HUB-OBSERVABILITY_STACK]
see_also: [HUB-API_GATEWAY, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-API_GATEWAY]
---

# Cross-Reference Link: api_gateway → observability_stack

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `api_gateway` depends on `observability_stack`.

## Source hub
- Hub: `api_gateway`
- Anchor: `HUB-API_GATEWAY`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
