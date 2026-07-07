---
id: SYNAPSE-00011
title: "Synapse: auth_service ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, auth_service, data_pipeline]
related: [HUB-AUTH_SERVICE, HUB-DATA_PIPELINE]
see_also: [HUB-AUTH_SERVICE, HUB-DATA_PIPELINE]
depends_on: [HUB-AUTH_SERVICE]
---

# Cross-Reference Link: auth_service → data_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `auth_service` documents `data_pipeline`.

## Source hub
- Hub: `auth_service`
- Anchor: `HUB-AUTH_SERVICE`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
