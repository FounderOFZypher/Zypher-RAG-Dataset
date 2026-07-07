---
id: CORTEX-L4
title: "Cortical Layer L4_reasoning"
doc_type: architecture_decision
category: rag
hub: coltex_knowledge_core
tags: [cortex, L4_reasoning, knowledge_architecture]
---

# Cortical Layer: L4_reasoning

**Role:** Multi-hop GraphRAG, synapse traversal, ADR chains

## Processing latency target
80ms

## Path
`cortex/L4-reasoning`

## Integration
Layer L4_reasoning feeds forward into the next cortical layer during retrieval pipeline execution.
Documents stored here carry elevated GraphRAG boost during neural routing.
