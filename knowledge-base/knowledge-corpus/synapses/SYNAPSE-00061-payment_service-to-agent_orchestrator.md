---
id: SYNAPSE-00061
title: "Synapse: payment_service ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, payment_service, agent_orchestrator]
related: [HUB-PAYMENT_SERVICE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-PAYMENT_SERVICE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Cross-Reference Link: payment_service → agent_orchestrator

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `payment_service` calls into `agent_orchestrator`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
