---
id: PATHWAY-0001
title: "Domain Pathway: frontal → temporal (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: frontal
lobe_target: temporal
pathway_type: inhibitory
tags: [pathway, inhibitory, frontal, temporal]
related: [LOBE-FRONTAL, LOBE-TEMPORAL]
see_also: [LOBE-FRONTAL, LOBE-TEMPORAL]
synthesizes: [LOBE-FRONTAL]
---

# Domain Pathway: frontal → temporal

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `frontal` connect to lobe `temporal` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-FRONTAL` (frontal)
- Target: `LOBE-TEMPORAL` (temporal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
