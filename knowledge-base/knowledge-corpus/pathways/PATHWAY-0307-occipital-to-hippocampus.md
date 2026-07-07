---
id: PATHWAY-0307
title: "Domain Pathway: occipital → hippocampus (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: occipital
lobe_target: hippocampus
pathway_type: excitatory
tags: [pathway, excitatory, occipital, hippocampus]
related: [LOBE-OCCIPITAL, LOBE-HIPPOCAMPUS]
see_also: [LOBE-OCCIPITAL, LOBE-HIPPOCAMPUS]
synthesizes: [LOBE-OCCIPITAL]
---

# Domain Pathway: occipital → hippocampus

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `occipital` connect to lobe `hippocampus` via this commissural pathway.

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
- Target: `LOBE-HIPPOCAMPUS` (hippocampus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
