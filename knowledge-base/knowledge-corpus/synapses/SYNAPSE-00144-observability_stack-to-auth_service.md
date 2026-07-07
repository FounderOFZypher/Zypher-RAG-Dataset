---
id: SYNAPSE-00144
title: "Synapse: observability_stack ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, observability_stack, auth_service]
related: [HUB-OBSERVABILITY_STACK, HUB-AUTH_SERVICE]
see_also: [HUB-OBSERVABILITY_STACK, HUB-AUTH_SERVICE]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Cross-Reference Link: observability_stack → auth_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**depends_on** — documents in `observability_stack` depends on `auth_service`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
