---
id: PATHWAY-0809
title: "Domain Pathway: thalamus → amygdala (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: thalamus
lobe_target: amygdala
pathway_type: modulatory
tags: [pathway, modulatory, thalamus, amygdala]
related: [LOBE-THALAMUS, LOBE-AMYGDALA]
see_also: [LOBE-THALAMUS, LOBE-AMYGDALA]
synthesizes: [LOBE-THALAMUS]
---

# Domain Pathway: thalamus → amygdala

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `thalamus` connect to lobe `amygdala` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-THALAMUS` (thalamus)
- Target: `LOBE-AMYGDALA` (amygdala)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
