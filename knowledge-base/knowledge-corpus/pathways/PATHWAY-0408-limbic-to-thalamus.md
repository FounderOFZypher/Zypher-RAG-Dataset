---
id: PATHWAY-0408
title: "Domain Pathway: limbic → thalamus (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: limbic
lobe_target: thalamus
pathway_type: modulatory
tags: [pathway, modulatory, limbic, thalamus]
related: [LOBE-LIMBIC, LOBE-THALAMUS]
see_also: [LOBE-LIMBIC, LOBE-THALAMUS]
synthesizes: [LOBE-LIMBIC]
---

# Domain Pathway: limbic → thalamus

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `limbic` connect to lobe `thalamus` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-LIMBIC` (limbic)
- Target: `LOBE-THALAMUS` (thalamus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
