---
id: PATHWAY-0508
title: "Domain Pathway: cerebellum → thalamus (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: cerebellum
lobe_target: thalamus
pathway_type: associative
tags: [pathway, associative, cerebellum, thalamus]
related: [LOBE-CEREBELLUM, LOBE-THALAMUS]
see_also: [LOBE-CEREBELLUM, LOBE-THALAMUS]
synthesizes: [LOBE-CEREBELLUM]
---

# Domain Pathway: cerebellum → thalamus

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `cerebellum` connect to lobe `thalamus` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-CEREBELLUM` (cerebellum)
- Target: `LOBE-THALAMUS` (thalamus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
