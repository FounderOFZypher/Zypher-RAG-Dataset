---
id: PATHWAY-0108
title: "Domain Pathway: temporal → thalamus (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: temporal
lobe_target: thalamus
pathway_type: commissural
tags: [pathway, commissural, temporal, thalamus]
related: [LOBE-TEMPORAL, LOBE-THALAMUS]
see_also: [LOBE-TEMPORAL, LOBE-THALAMUS]
synthesizes: [LOBE-TEMPORAL]
---

# Domain Pathway: temporal → thalamus

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `temporal` connect to lobe `thalamus` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-TEMPORAL` (temporal)
- Target: `LOBE-THALAMUS` (thalamus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
