---
id: CORTEX-L3
title: "Cortical Layer L3_integration"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [cortex, L3_integration, knowledge_architecture]
---

# Cortical Layer: L3_integration

**Role:** Cross-domain pattern matching, hub assignment

## Processing latency target
30ms

## Path
`cortex/L3-integration`

## Integration
Layer L3_integration feeds forward into the next cortical layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during neural routing.
