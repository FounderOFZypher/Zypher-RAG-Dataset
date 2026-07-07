---
id: PATHWAY-0801
title: "Domain Pathway: thalamus → temporal (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: thalamus
lobe_target: temporal
pathway_type: commissural
tags: [pathway, commissural, thalamus, temporal]
related: [LOBE-THALAMUS, LOBE-TEMPORAL]
see_also: [LOBE-THALAMUS, LOBE-TEMPORAL]
synthesizes: [LOBE-THALAMUS]
---

# Domain Pathway: thalamus → temporal

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `thalamus` connect to lobe `temporal` via this commissural pathway.

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
- Target: `LOBE-TEMPORAL` (temporal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
