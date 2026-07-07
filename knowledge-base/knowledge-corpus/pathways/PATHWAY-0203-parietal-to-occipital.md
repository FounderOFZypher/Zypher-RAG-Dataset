---
id: PATHWAY-0203
title: "Domain Pathway: parietal → occipital (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: parietal
lobe_target: occipital
pathway_type: excitatory
tags: [pathway, excitatory, parietal, occipital]
related: [LOBE-PARIETAL, LOBE-OCCIPITAL]
see_also: [LOBE-PARIETAL, LOBE-OCCIPITAL]
synthesizes: [LOBE-PARIETAL]
---

# Domain Pathway: parietal → occipital

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `parietal` connect to lobe `occipital` via this commissural pathway.

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
- Target: `LOBE-OCCIPITAL` (occipital)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
