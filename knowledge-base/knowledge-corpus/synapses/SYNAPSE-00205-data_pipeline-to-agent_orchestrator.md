---
id: SYNAPSE-00205
title: "Synapse: data_pipeline ↔ agent_orchestrator"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, data_pipeline, agent_orchestrator]
related: [HUB-DATA_PIPELINE, HUB-AGENT_ORCHESTRATOR]
see_also: [HUB-DATA_PIPELINE, HUB-AGENT_ORCHESTRATOR]
depends_on: [HUB-DATA_PIPELINE]
---

# Cross-Reference Link: data_pipeline → agent_orchestrator

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**calls** — documents in `data_pipeline` calls into `agent_orchestrator`.

## Source hub
- Hub: `data_pipeline`
- Anchor: `HUB-DATA_PIPELINE`

## Target hub
- Hub: `agent_orchestrator`
- Anchor: `HUB-AGENT_ORCHESTRATOR`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
