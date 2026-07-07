---
id: CORTEX-L1
title: "Cortical Layer L1_sensory"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [cortex, L1_sensory, knowledge_architecture]
---

# Cortical Layer: L1_sensory

**Role:** Raw document ingestion signals, chunk boundaries, embedding triggers

## Processing latency target
5ms

## Path
`cortex/L1-sensory`

## Integration
Layer L1_sensory feeds forward into the next cortical layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during neural routing.
