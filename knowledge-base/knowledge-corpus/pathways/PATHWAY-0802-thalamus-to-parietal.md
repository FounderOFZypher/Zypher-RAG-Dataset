---
id: PATHWAY-0802
title: "Domain Pathway: thalamus → parietal (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: thalamus
lobe_target: parietal
pathway_type: excitatory
tags: [pathway, excitatory, thalamus, parietal]
related: [LOBE-THALAMUS, LOBE-PARIETAL]
see_also: [LOBE-THALAMUS, LOBE-PARIETAL]
synthesizes: [LOBE-THALAMUS]
---

# Domain Pathway: thalamus → parietal

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `thalamus` connect to lobe `parietal` via this commissural pathway.

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
- Target: `LOBE-PARIETAL` (parietal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
