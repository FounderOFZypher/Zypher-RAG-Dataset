---
id: SYNAPSE-00017
title: "Synapse: auth_service ↔ coltex_knowledge_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, coltex_knowledge_core]
related: [HUB-AUTH_SERVICE, HUB-COLTEX_KNOWLEDGE_CORE]
see_also: [HUB-AUTH_SERVICE, HUB-COLTEX_KNOWLEDGE_CORE]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → coltex_knowledge_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `auth_service` is related to `coltex_knowledge_core`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `coltex_knowledge_core`
- Anchor: `HUB-COLTEX_KNOWLEDGE_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
