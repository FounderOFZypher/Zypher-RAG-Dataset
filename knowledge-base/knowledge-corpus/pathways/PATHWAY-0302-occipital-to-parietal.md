---
id: PATHWAY-0302
title: "Domain Pathway: occipital → parietal (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: occipital
lobe_target: parietal
pathway_type: excitatory
tags: [pathway, excitatory, occipital, parietal]
related: [LOBE-OCCIPITAL, LOBE-PARIETAL]
see_also: [LOBE-OCCIPITAL, LOBE-PARIETAL]
synthesizes: [LOBE-OCCIPITAL]
---

# Domain Pathway: occipital → parietal

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `occipital` connect to lobe `parietal` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-OCCIPITAL` (occipital)
- Target: `LOBE-PARIETAL` (parietal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
