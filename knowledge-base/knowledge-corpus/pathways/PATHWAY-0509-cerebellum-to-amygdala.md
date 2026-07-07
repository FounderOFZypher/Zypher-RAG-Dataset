---
id: PATHWAY-0509
title: "Domain Pathway: cerebellum → amygdala (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: cerebellum
lobe_target: amygdala
pathway_type: commissural
tags: [pathway, commissural, cerebellum, amygdala]
related: [LOBE-CEREBELLUM, LOBE-AMYGDALA]
see_also: [LOBE-CEREBELLUM, LOBE-AMYGDALA]
synthesizes: [LOBE-CEREBELLUM]
---

# Domain Pathway: cerebellum → amygdala

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `cerebellum` connect to lobe `amygdala` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-CEREBELLUM` (cerebellum)
- Target: `LOBE-AMYGDALA` (amygdala)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
