---
id: PATHWAY-0805
title: "Domain Pathway: thalamus → cerebellum (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: thalamus
lobe_target: cerebellum
pathway_type: associative
tags: [pathway, associative, thalamus, cerebellum]
related: [LOBE-THALAMUS, LOBE-CEREBELLUM]
see_also: [LOBE-THALAMUS, LOBE-CEREBELLUM]
synthesizes: [LOBE-THALAMUS]
---

# Domain Pathway: thalamus → cerebellum

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `thalamus` connect to lobe `cerebellum` via this commissural pathway.

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
- Target: `LOBE-CEREBELLUM` (cerebellum)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
