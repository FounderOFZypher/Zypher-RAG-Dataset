---
id: PATHWAY-0300
title: "Domain Pathway: occipital → frontal (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: occipital
lobe_target: frontal
pathway_type: associative
tags: [pathway, associative, occipital, frontal]
related: [LOBE-OCCIPITAL, LOBE-FRONTAL]
see_also: [LOBE-OCCIPITAL, LOBE-FRONTAL]
synthesizes: [LOBE-OCCIPITAL]
---

# Domain Pathway: occipital → frontal

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `occipital` connect to lobe `frontal` via this commissural pathway.

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
- Target: `LOBE-FRONTAL` (frontal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
