---
id: PATHWAY-0309
title: "Domain Pathway: occipital → amygdala (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: occipital
lobe_target: amygdala
pathway_type: modulatory
tags: [pathway, modulatory, occipital, amygdala]
related: [LOBE-OCCIPITAL, LOBE-AMYGDALA]
see_also: [LOBE-OCCIPITAL, LOBE-AMYGDALA]
synthesizes: [LOBE-OCCIPITAL]
---

# Domain Pathway: occipital → amygdala

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `occipital` connect to lobe `amygdala` via this commissural pathway.

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
- Target: `LOBE-AMYGDALA` (amygdala)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
