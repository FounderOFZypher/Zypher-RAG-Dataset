---
id: CORTEX-L2
title: "Cortical Layer L2_association"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [cortex, L2_association, knowledge_architecture]
---

# Cortical Layer: L2_association

**Role:** Domain tagging, metadata extraction, initial graph edges

## Processing latency target
15ms

## Path
`cortex/L2-association`

## Integration
Layer L2_association feeds forward into the next cortical layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during neural routing.
