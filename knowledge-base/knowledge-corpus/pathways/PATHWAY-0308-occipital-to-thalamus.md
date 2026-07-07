---
id: PATHWAY-0308
title: "Domain Pathway: occipital → thalamus (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: occipital
lobe_target: thalamus
pathway_type: inhibitory
tags: [pathway, inhibitory, occipital, thalamus]
related: [LOBE-OCCIPITAL, LOBE-THALAMUS]
see_also: [LOBE-OCCIPITAL, LOBE-THALAMUS]
synthesizes: [LOBE-OCCIPITAL]
---

# Domain Pathway: occipital → thalamus

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `occipital` connect to lobe `thalamus` via this commissural pathway.

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
- Target: `LOBE-THALAMUS` (thalamus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
