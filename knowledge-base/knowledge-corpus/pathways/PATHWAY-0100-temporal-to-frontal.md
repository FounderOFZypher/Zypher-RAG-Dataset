---
id: PATHWAY-0100
title: "Domain Pathway: temporal → frontal (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: temporal
lobe_target: frontal
pathway_type: inhibitory
tags: [pathway, inhibitory, temporal, frontal]
related: [LOBE-TEMPORAL, LOBE-FRONTAL]
see_also: [LOBE-TEMPORAL, LOBE-FRONTAL]
synthesizes: [LOBE-TEMPORAL]
---

# Domain Pathway: temporal → frontal

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `temporal` connect to lobe `frontal` via this commissural pathway.

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
- Target: `LOBE-FRONTAL` (frontal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
