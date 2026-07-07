---
id: PATHWAY-0609
title: "Domain Pathway: brainstem → amygdala (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: brainstem
lobe_target: amygdala
pathway_type: excitatory
tags: [pathway, excitatory, brainstem, amygdala]
related: [LOBE-BRAINSTEM, LOBE-AMYGDALA]
see_also: [LOBE-BRAINSTEM, LOBE-AMYGDALA]
synthesizes: [LOBE-BRAINSTEM]
---

# Domain Pathway: brainstem → amygdala

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `brainstem` connect to lobe `amygdala` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-BRAINSTEM` (brainstem)
- Target: `LOBE-AMYGDALA` (amygdala)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
