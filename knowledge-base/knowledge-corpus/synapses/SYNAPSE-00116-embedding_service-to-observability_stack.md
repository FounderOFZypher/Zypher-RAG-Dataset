---
id: SYNAPSE-00116
title: "Synapse: embedding_service ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, embedding_service, observability_stack]
related: [HUB-EMBEDDING_SERVICE, HUB-OBSERVABILITY_STACK]
see_also: [HUB-EMBEDDING_SERVICE, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-EMBEDDING_SERVICE]
---

# Cross-Reference Link: embedding_service → observability_stack

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `embedding_service` calls into `observability_stack`.

## Source hub
- Hub: `embedding_service`
- Anchor: `HUB-EMBEDDING_SERVICE`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
