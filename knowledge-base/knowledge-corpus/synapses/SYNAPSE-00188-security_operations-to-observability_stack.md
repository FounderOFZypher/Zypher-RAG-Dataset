---
id: SYNAPSE-00188
title: "Synapse: security_operations ↔ observability_stack"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, security_operations, observability_stack]
related: [HUB-SECURITY_OPERATIONS, HUB-OBSERVABILITY_STACK]
see_also: [HUB-SECURITY_OPERATIONS, HUB-OBSERVABILITY_STACK]
depends_on: [HUB-SECURITY_OPERATIONS]
---

# Cross-Reference Link: security_operations → observability_stack

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `security_operations` calls into `observability_stack`.

## Source hub
- Hub: `security_operations`
- Anchor: `HUB-SECURITY_OPERATIONS`

## Target hub
- Hub: `observability_stack`
- Anchor: `HUB-OBSERVABILITY_STACK`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
