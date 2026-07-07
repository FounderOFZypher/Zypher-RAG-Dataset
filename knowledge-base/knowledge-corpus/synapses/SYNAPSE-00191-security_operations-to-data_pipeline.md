---
id: SYNAPSE-00191
title: "Synapse: security_operations ↔ data_pipeline"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, security_operations, data_pipeline]
related: [HUB-SECURITY_OPERATIONS, HUB-DATA_PIPELINE]
see_also: [HUB-SECURITY_OPERATIONS, HUB-DATA_PIPELINE]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Cross-Reference Link: security_operations → data_pipeline

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `security_operations` is related to `data_pipeline`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
