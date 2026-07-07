---
id: PATHWAY-0804
title: "Domain Pathway: thalamus → limbic (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: thalamus
lobe_target: limbic
pathway_type: modulatory
tags: [pathway, modulatory, thalamus, limbic]
related: [LOBE-THALAMUS, LOBE-LIMBIC]
see_also: [LOBE-THALAMUS, LOBE-LIMBIC]
synthesizes: [LOBE-THALAMUS]
---

# Domain Pathway: thalamus → limbic

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `thalamus` connect to lobe `limbic` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-THALAMUS` (thalamus)
- Target: `LOBE-LIMBIC` (limbic)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
