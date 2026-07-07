---
id: PATHWAY-0002
title: "Domain Pathway: frontal → parietal (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: frontal
lobe_target: parietal
pathway_type: modulatory
tags: [pathway, modulatory, frontal, parietal]
related: [LOBE-FRONTAL, LOBE-PARIETAL]
see_also: [LOBE-FRONTAL, LOBE-PARIETAL]
synthesizes: [LOBE-FRONTAL]
---

# Domain Pathway: frontal → parietal

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `frontal` connect to lobe `parietal` via this commissural pathway.

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
- Target: `LOBE-PARIETAL` (parietal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
