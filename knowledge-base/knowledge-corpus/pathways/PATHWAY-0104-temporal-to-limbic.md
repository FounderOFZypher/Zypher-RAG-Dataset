---
id: PATHWAY-0104
title: "Domain Pathway: temporal → limbic (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: temporal
lobe_target: limbic
pathway_type: excitatory
tags: [pathway, excitatory, temporal, limbic]
related: [LOBE-TEMPORAL, LOBE-LIMBIC]
see_also: [LOBE-TEMPORAL, LOBE-LIMBIC]
synthesizes: [LOBE-TEMPORAL]
---

# Domain Pathway: temporal → limbic

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `temporal` connect to lobe `limbic` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-TEMPORAL` (temporal)
- Target: `LOBE-LIMBIC` (limbic)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
