---
id: PATHWAY-0409
title: "Domain Pathway: limbic → amygdala (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: limbic
lobe_target: amygdala
pathway_type: associative
tags: [pathway, associative, limbic, amygdala]
related: [LOBE-LIMBIC, LOBE-AMYGDALA]
see_also: [LOBE-LIMBIC, LOBE-AMYGDALA]
synthesizes: [LOBE-LIMBIC]
---

# Domain Pathway: limbic → amygdala

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `limbic` connect to lobe `amygdala` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-LIMBIC` (limbic)
- Target: `LOBE-AMYGDALA` (amygdala)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
