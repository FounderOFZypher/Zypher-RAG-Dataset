---
id: PATHWAY-0207
title: "Domain Pathway: parietal → hippocampus (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: parietal
lobe_target: hippocampus
pathway_type: commissural
tags: [pathway, commissural, parietal, hippocampus]
related: [LOBE-PARIETAL, LOBE-HIPPOCAMPUS]
see_also: [LOBE-PARIETAL, LOBE-HIPPOCAMPUS]
synthesizes: [LOBE-PARIETAL]
---

# Domain Pathway: parietal → hippocampus

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `parietal` connect to lobe `hippocampus` via this commissural pathway.

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
- Target: `LOBE-HIPPOCAMPUS` (hippocampus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
