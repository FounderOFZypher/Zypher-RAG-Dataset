---
id: PATHWAY-0702
title: "Domain Pathway: hippocampus → parietal (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: hippocampus
lobe_target: parietal
pathway_type: commissural
tags: [pathway, commissural, hippocampus, parietal]
related: [LOBE-HIPPOCAMPUS, LOBE-PARIETAL]
see_also: [LOBE-HIPPOCAMPUS, LOBE-PARIETAL]
synthesizes: [LOBE-HIPPOCAMPUS]
---

# Domain Pathway: hippocampus → parietal

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `hippocampus` connect to lobe `parietal` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-HIPPOCAMPUS` (hippocampus)
- Target: `LOBE-PARIETAL` (parietal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
