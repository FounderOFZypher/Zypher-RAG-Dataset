---
id: CORTEX-L5
title: "Cortical Layer L5_executive"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [cortex, L5_executive, knowledge_architecture]
---

# Cortical Layer: L5_executive

**Role:** Context assembly, reranking, faithfulness checks

## Processing latency target
120ms

## Path
`cortex/L5-executive`

## Integration
Layer L5_executive feeds forward into the next cortical layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during neural routing.
