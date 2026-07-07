---
id: PATHWAY-0209
title: "Domain Pathway: parietal → amygdala (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: parietal
lobe_target: amygdala
pathway_type: inhibitory
tags: [pathway, inhibitory, parietal, amygdala]
related: [LOBE-PARIETAL, LOBE-AMYGDALA]
see_also: [LOBE-PARIETAL, LOBE-AMYGDALA]
synthesizes: [LOBE-PARIETAL]
---

# Domain Pathway: parietal → amygdala

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `parietal` connect to lobe `amygdala` via this commissural pathway.

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
- Target: `LOBE-AMYGDALA` (amygdala)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
