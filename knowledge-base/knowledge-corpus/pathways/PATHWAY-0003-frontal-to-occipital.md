---
id: PATHWAY-0003
title: "Domain Pathway: frontal → occipital (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: frontal
lobe_target: occipital
pathway_type: associative
tags: [pathway, associative, frontal, occipital]
related: [LOBE-FRONTAL, LOBE-OCCIPITAL]
see_also: [LOBE-FRONTAL, LOBE-OCCIPITAL]
synthesizes: [LOBE-FRONTAL]
---

# Domain Pathway: frontal → occipital

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `frontal` connect to lobe `occipital` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-FRONTAL` (frontal)
- Target: `LOBE-OCCIPITAL` (occipital)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
