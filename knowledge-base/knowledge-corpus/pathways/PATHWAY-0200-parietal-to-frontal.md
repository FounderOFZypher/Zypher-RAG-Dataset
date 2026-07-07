---
id: PATHWAY-0200
title: "Domain Pathway: parietal → frontal (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: parietal
lobe_target: frontal
pathway_type: modulatory
tags: [pathway, modulatory, parietal, frontal]
related: [LOBE-PARIETAL, LOBE-FRONTAL]
see_also: [LOBE-PARIETAL, LOBE-FRONTAL]
synthesizes: [LOBE-PARIETAL]
---

# Domain Pathway: parietal → frontal

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `parietal` connect to lobe `frontal` via this commissural pathway.

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
- Target: `LOBE-FRONTAL` (frontal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
