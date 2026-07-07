---
id: SYNAPSE-00001
title: "Synapse: auth_service ↔ indexing_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, indexing_pipeline]
related: [HUB-AUTH_SERVICE, HUB-INDEXING_PIPELINE]
see_also: [HUB-AUTH_SERVICE, HUB-INDEXING_PIPELINE]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → indexing_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `auth_service` is related to `indexing_pipeline`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
