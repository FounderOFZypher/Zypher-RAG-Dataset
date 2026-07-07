---
id: PATHWAY-0504
title: "Domain Pathway: cerebellum → limbic (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: cerebellum
lobe_target: limbic
pathway_type: commissural
tags: [pathway, commissural, cerebellum, limbic]
related: [LOBE-CEREBELLUM, LOBE-LIMBIC]
see_also: [LOBE-CEREBELLUM, LOBE-LIMBIC]
synthesizes: [LOBE-CEREBELLUM]
---

# Domain Pathway: cerebellum → limbic

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `cerebellum` connect to lobe `limbic` via this commissural pathway.

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
- Target: `LOBE-LIMBIC` (limbic)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
