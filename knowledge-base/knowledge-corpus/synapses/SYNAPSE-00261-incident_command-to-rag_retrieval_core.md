---
id: SYNAPSE-00261
title: "Synapse: incident_command ↔ rag_retrieval_core"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, incident_command, rag_retrieval_core]
related: [HUB-INCIDENT_COMMAND, HUB-RAG_RETRIEVAL_CORE]
see_also: [HUB-INCIDENT_COMMAND, HUB-RAG_RETRIEVAL_CORE]
depends_on: [HUB-INCIDENT_COMMAND]
---

# Cross-Reference Link: incident_command → rag_retrieval_core

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**documents** — documents in `incident_command` documents `rag_retrieval_core`.

## Source hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Target hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
