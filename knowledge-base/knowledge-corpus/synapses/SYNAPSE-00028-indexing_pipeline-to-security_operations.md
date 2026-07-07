---
id: SYNAPSE-00028
title: "Synapse: indexing_pipeline ↔ security_operations"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, indexing_pipeline, security_operations]
related: [HUB-INDEXING_PIPELINE, HUB-SECURITY_OPERATIONS]
see_also: [HUB-INDEXING_PIPELINE, HUB-SECURITY_OPERATIONS]
depends_on: [HUB-INDEXING_PIPELINE]
---

# Cross-Reference Link: indexing_pipeline → security_operations

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `indexing_pipeline` documents `security_operations`.

## Source hub
- Hub: `indexing_pipeline`
- Anchor: `HUB-INDEXING_PIPELINE`

## Target hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
