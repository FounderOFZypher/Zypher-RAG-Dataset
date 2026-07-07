---
id: PATHWAY-0005
title: "Domain Pathway: frontal → cerebellum (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: frontal
lobe_target: cerebellum
pathway_type: excitatory
tags: [pathway, excitatory, frontal, cerebellum]
related: [LOBE-FRONTAL, LOBE-CEREBELLUM]
see_also: [LOBE-FRONTAL, LOBE-CEREBELLUM]
synthesizes: [LOBE-FRONTAL]
---

# Domain Pathway: frontal → cerebellum

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `frontal` connect to lobe `cerebellum` via this commissural pathway.

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
- Target: `LOBE-CEREBELLUM` (cerebellum)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
