---
id: PATHWAY-0800
title: "Domain Pathway: thalamus → frontal (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: thalamus
lobe_target: frontal
pathway_type: associative
tags: [pathway, associative, thalamus, frontal]
related: [LOBE-THALAMUS, LOBE-FRONTAL]
see_also: [LOBE-THALAMUS, LOBE-FRONTAL]
synthesizes: [LOBE-THALAMUS]
---

# Domain Pathway: thalamus → frontal

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `thalamus` connect to lobe `frontal` via this commissural pathway.

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
- Target: `LOBE-FRONTAL` (frontal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
