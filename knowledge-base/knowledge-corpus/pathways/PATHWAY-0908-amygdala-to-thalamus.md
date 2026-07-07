---
id: PATHWAY-0908
title: "Domain Pathway: amygdala → thalamus (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: amygdala
lobe_target: thalamus
pathway_type: modulatory
tags: [pathway, modulatory, amygdala, thalamus]
related: [LOBE-AMYGDALA, LOBE-THALAMUS]
see_also: [LOBE-AMYGDALA, LOBE-THALAMUS]
synthesizes: [LOBE-AMYGDALA]
---

# Domain Pathway: amygdala → thalamus

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `amygdala` connect to lobe `thalamus` via this commissural pathway.

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
- Target: `LOBE-THALAMUS` (thalamus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
