---
id: PATHWAY-0305
title: "Domain Pathway: occipital → cerebellum (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: occipital
lobe_target: cerebellum
pathway_type: associative
tags: [pathway, associative, occipital, cerebellum]
related: [LOBE-OCCIPITAL, LOBE-CEREBELLUM]
see_also: [LOBE-OCCIPITAL, LOBE-CEREBELLUM]
synthesizes: [LOBE-OCCIPITAL]
---

# Domain Pathway: occipital → cerebellum

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `occipital` connect to lobe `cerebellum` via this commissural pathway.

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
- Target: `LOBE-CEREBELLUM` (cerebellum)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
