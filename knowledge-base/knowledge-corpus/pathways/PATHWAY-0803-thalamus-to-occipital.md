---
id: PATHWAY-0803
title: "Domain Pathway: thalamus → occipital (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: thalamus
lobe_target: occipital
pathway_type: inhibitory
tags: [pathway, inhibitory, thalamus, occipital]
related: [LOBE-THALAMUS, LOBE-OCCIPITAL]
see_also: [LOBE-THALAMUS, LOBE-OCCIPITAL]
synthesizes: [LOBE-THALAMUS]
---

# Domain Pathway: thalamus → occipital

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `thalamus` connect to lobe `occipital` via this commissural pathway.

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
- Target: `LOBE-OCCIPITAL` (occipital)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
