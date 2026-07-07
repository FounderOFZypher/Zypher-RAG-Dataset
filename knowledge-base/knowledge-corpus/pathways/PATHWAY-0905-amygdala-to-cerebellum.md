---
id: PATHWAY-0905
title: "Domain Pathway: amygdala → cerebellum (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: amygdala
lobe_target: cerebellum
pathway_type: commissural
tags: [pathway, commissural, amygdala, cerebellum]
related: [LOBE-AMYGDALA, LOBE-CEREBELLUM]
see_also: [LOBE-AMYGDALA, LOBE-CEREBELLUM]
synthesizes: [LOBE-AMYGDALA]
---

# Domain Pathway: amygdala → cerebellum

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `amygdala` connect to lobe `cerebellum` via this commissural pathway.

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
- Target: `LOBE-CEREBELLUM` (cerebellum)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
