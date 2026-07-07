---
id: PATHWAY-0301
title: "Domain Pathway: occipital → temporal (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: occipital
lobe_target: temporal
pathway_type: commissural
tags: [pathway, commissural, occipital, temporal]
related: [LOBE-OCCIPITAL, LOBE-TEMPORAL]
see_also: [LOBE-OCCIPITAL, LOBE-TEMPORAL]
synthesizes: [LOBE-OCCIPITAL]
---

# Domain Pathway: occipital → temporal

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `occipital` connect to lobe `temporal` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-OCCIPITAL` (occipital)
- Target: `LOBE-TEMPORAL` (temporal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
