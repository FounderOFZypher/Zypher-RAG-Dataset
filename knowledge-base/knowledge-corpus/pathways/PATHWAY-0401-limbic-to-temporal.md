---
id: PATHWAY-0401
title: "Domain Pathway: limbic → temporal (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: limbic
lobe_target: temporal
pathway_type: excitatory
tags: [pathway, excitatory, limbic, temporal]
related: [LOBE-LIMBIC, LOBE-TEMPORAL]
see_also: [LOBE-LIMBIC, LOBE-TEMPORAL]
synthesizes: [LOBE-LIMBIC]
---

# Domain Pathway: limbic → temporal

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `limbic` connect to lobe `temporal` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-LIMBIC` (limbic)
- Target: `LOBE-TEMPORAL` (temporal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
