---
id: PATHWAY-0906
title: "Domain Pathway: amygdala → brainstem (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: amygdala
lobe_target: brainstem
pathway_type: excitatory
tags: [pathway, excitatory, amygdala, brainstem]
related: [LOBE-AMYGDALA, LOBE-BRAINSTEM]
see_also: [LOBE-AMYGDALA, LOBE-BRAINSTEM]
synthesizes: [LOBE-AMYGDALA]
---

# Domain Pathway: amygdala → brainstem

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `amygdala` connect to lobe `brainstem` via this commissural pathway.

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
- Target: `LOBE-BRAINSTEM` (brainstem)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
