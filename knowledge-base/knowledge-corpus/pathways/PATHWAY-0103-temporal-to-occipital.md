---
id: PATHWAY-0103
title: "Domain Pathway: temporal → occipital (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: temporal
lobe_target: occipital
pathway_type: commissural
tags: [pathway, commissural, temporal, occipital]
related: [LOBE-TEMPORAL, LOBE-OCCIPITAL]
see_also: [LOBE-TEMPORAL, LOBE-OCCIPITAL]
synthesizes: [LOBE-TEMPORAL]
---

# Domain Pathway: temporal → occipital

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `temporal` connect to lobe `occipital` via this commissural pathway.

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
- Target: `LOBE-OCCIPITAL` (occipital)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
