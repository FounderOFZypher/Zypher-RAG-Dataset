---
id: PATHWAY-0009
title: "Domain Pathway: frontal → amygdala (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: frontal
lobe_target: amygdala
pathway_type: commissural
tags: [pathway, commissural, frontal, amygdala]
related: [LOBE-FRONTAL, LOBE-AMYGDALA]
see_also: [LOBE-FRONTAL, LOBE-AMYGDALA]
synthesizes: [LOBE-FRONTAL]
---

# Domain Pathway: frontal → amygdala

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `frontal` connect to lobe `amygdala` via this commissural pathway.

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
- Target: `LOBE-AMYGDALA` (amygdala)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
