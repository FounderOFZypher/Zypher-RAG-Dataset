---
id: SYNAPSE-00044
title: "Synapse: graphrag_engine ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, graphrag_engine, observability_stack]
related: [HUB-GRAPHRAG_ENGINE, HUB-OBSERVABILITY_STACK]
see_also: [HUB-GRAPHRAG_ENGINE, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-GRAPHRAG_ENGINE]
---

# Cross-Reference Link: graphrag_engine → observability_stack

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `graphrag_engine` calls into `observability_stack`.

## Source hub
- Hub: `graphrag_engine`
- Anchor: `HUB-GRAPHRAG_ENGINE`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
