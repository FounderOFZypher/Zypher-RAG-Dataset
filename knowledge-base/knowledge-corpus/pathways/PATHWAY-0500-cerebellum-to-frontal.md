---
id: PATHWAY-0500
title: "Domain Pathway: cerebellum → frontal (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: cerebellum
lobe_target: frontal
pathway_type: excitatory
tags: [pathway, excitatory, cerebellum, frontal]
related: [LOBE-CEREBELLUM, LOBE-FRONTAL]
see_also: [LOBE-CEREBELLUM, LOBE-FRONTAL]
synthesizes: [LOBE-CEREBELLUM]
---

# Domain Pathway: cerebellum → frontal

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `cerebellum` connect to lobe `frontal` via this commissural pathway.

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
- Target: `LOBE-FRONTAL` (frontal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
