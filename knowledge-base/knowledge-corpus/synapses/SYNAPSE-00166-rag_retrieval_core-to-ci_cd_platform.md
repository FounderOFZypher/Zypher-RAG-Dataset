---
id: SYNAPSE-00166
title: "Synapse: rag_retrieval_core ↔ ci_cd_platform"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, rag_retrieval_core, ci_cd_platform]
related: [HUB-RAG_RETRIEVAL_CORE, HUB-CI_CD_PLATFORM]
see_also: [HUB-RAG_RETRIEVAL_CORE, HUB-CI_CD_PLATFORM]
depends_on: [HUB-RAG_RETRIEVAL_CORE]
---

# Cross-Reference Link: rag_retrieval_core → ci_cd_platform

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `rag_retrieval_core` is related to `ci_cd_platform`.

## Source hub
- Hub: `rag_retrieval_core`
- Anchor: `HUB-RAG_RETRIEVAL_CORE`

## Target hub
- Hub: `ci_cd_platform`
- Anchor: `HUB-CI_CD_PLATFORM`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
