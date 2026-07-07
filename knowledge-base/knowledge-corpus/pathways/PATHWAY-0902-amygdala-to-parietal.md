---
id: PATHWAY-0902
title: "Domain Pathway: amygdala → parietal (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: amygdala
lobe_target: parietal
pathway_type: inhibitory
tags: [pathway, inhibitory, amygdala, parietal]
related: [LOBE-AMYGDALA, LOBE-PARIETAL]
see_also: [LOBE-AMYGDALA, LOBE-PARIETAL]
synthesizes: [LOBE-AMYGDALA]
---

# Domain Pathway: amygdala → parietal

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `amygdala` connect to lobe `parietal` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-AMYGDALA` (amygdala)
- Target: `LOBE-PARIETAL` (parietal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
