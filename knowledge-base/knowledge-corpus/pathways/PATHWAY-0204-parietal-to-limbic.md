---
id: PATHWAY-0204
title: "Domain Pathway: parietal → limbic (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: parietal
lobe_target: limbic
pathway_type: inhibitory
tags: [pathway, inhibitory, parietal, limbic]
related: [LOBE-PARIETAL, LOBE-LIMBIC]
see_also: [LOBE-PARIETAL, LOBE-LIMBIC]
synthesizes: [LOBE-PARIETAL]
---

# Domain Pathway: parietal → limbic

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `parietal` connect to lobe `limbic` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-PARIETAL` (parietal)
- Target: `LOBE-LIMBIC` (limbic)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
