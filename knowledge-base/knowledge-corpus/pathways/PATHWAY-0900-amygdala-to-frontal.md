---
id: PATHWAY-0900
title: "Domain Pathway: amygdala → frontal (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: amygdala
lobe_target: frontal
pathway_type: commissural
tags: [pathway, commissural, amygdala, frontal]
related: [LOBE-AMYGDALA, LOBE-FRONTAL]
see_also: [LOBE-AMYGDALA, LOBE-FRONTAL]
synthesizes: [LOBE-AMYGDALA]
---

# Domain Pathway: amygdala → frontal

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `amygdala` connect to lobe `frontal` via this commissural pathway.

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
- Target: `LOBE-FRONTAL` (frontal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
