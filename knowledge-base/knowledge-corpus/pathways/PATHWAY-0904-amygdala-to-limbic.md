---
id: PATHWAY-0904
title: "Domain Pathway: amygdala → limbic (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: amygdala
lobe_target: limbic
pathway_type: associative
tags: [pathway, associative, amygdala, limbic]
related: [LOBE-AMYGDALA, LOBE-LIMBIC]
see_also: [LOBE-AMYGDALA, LOBE-LIMBIC]
synthesizes: [LOBE-AMYGDALA]
---

# Domain Pathway: amygdala → limbic

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `amygdala` connect to lobe `limbic` via this commissural pathway.

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
- Target: `LOBE-LIMBIC` (limbic)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
