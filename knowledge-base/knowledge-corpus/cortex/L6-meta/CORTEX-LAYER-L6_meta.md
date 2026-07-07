---
id: CORTEX-L6
title: "Cortical Layer L6_meta"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [cortex, L6_meta, knowledge_architecture]
---

# Cortical Layer: L6_meta

**Role:** Brain identity, architecture docs, pulse orchestration

## Processing latency target
200ms

## Path
`cortex/L6-meta`

## Integration
Layer L6_meta feeds forward into the next cortical layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during neural routing.
