---
id: PATHWAY-0304
title: "Domain Pathway: occipital → limbic (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: occipital
lobe_target: limbic
pathway_type: modulatory
tags: [pathway, modulatory, occipital, limbic]
related: [LOBE-OCCIPITAL, LOBE-LIMBIC]
see_also: [LOBE-OCCIPITAL, LOBE-LIMBIC]
synthesizes: [LOBE-OCCIPITAL]
---

# Domain Pathway: occipital → limbic

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `occipital` connect to lobe `limbic` via this commissural pathway.

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
- Target: `LOBE-LIMBIC` (limbic)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
