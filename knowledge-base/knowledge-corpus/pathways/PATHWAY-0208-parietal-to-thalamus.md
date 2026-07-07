---
id: PATHWAY-0208
title: "Domain Pathway: parietal → thalamus (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: parietal
lobe_target: thalamus
pathway_type: excitatory
tags: [pathway, excitatory, parietal, thalamus]
related: [LOBE-PARIETAL, LOBE-THALAMUS]
see_also: [LOBE-PARIETAL, LOBE-THALAMUS]
synthesizes: [LOBE-PARIETAL]
---

# Domain Pathway: parietal → thalamus

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `parietal` connect to lobe `thalamus` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-PARIETAL` (parietal)
- Target: `LOBE-THALAMUS` (thalamus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
