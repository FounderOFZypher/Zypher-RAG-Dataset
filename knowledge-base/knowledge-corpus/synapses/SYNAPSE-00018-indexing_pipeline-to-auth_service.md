---
id: SYNAPSE-00018
title: "Synapse: indexing_pipeline ↔ auth_service"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, indexing_pipeline, auth_service]
related: [HUB-INDEXING_PIPELINE, HUB-AUTH_SERVICE]
see_also: [HUB-INDEXING_PIPELINE, HUB-AUTH_SERVICE]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Cross-Reference Link: indexing_pipeline → auth_service

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `indexing_pipeline` is related to `auth_service`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
