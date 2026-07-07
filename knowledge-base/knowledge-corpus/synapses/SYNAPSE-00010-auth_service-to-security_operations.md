---
id: SYNAPSE-00010
title: "Synapse: auth_service ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, security_operations]
related: [HUB-AUTH_SERVICE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-AUTH_SERVICE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → security_operations

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `auth_service` calls into `security_operations`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
