---
id: SYNAPSE-00146
title: "Synapse: observability_stack ↔ graphrag_engine"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, observability_stack, graphrag_engine]
related: [HUB-OBSERVABILITY_STACK, HUB-GRAPHRAG_ENGINE]
see_also: [HUB-OBSERVABILITY_STACK, HUB-GRAPHRAG_ENGINE]
depends_on: [HUB-OBSERVABILITY_STACK]
---

# Cross-Reference Link: observability_stack → graphrag_engine

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `observability_stack` calls into `graphrag_engine`.

## Source hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Target hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
