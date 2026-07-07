---
id: PATHWAY-0406
title: "Domain Pathway: limbic → brainstem (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: limbic
lobe_target: brainstem
pathway_type: excitatory
tags: [pathway, excitatory, limbic, brainstem]
related: [LOBE-LIMBIC, LOBE-BRAINSTEM]
see_also: [LOBE-LIMBIC, LOBE-BRAINSTEM]
synthesizes: [LOBE-LIMBIC]
---

# Domain Pathway: limbic → brainstem

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `limbic` connect to lobe `brainstem` via this commissural pathway.

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
- Target: `LOBE-BRAINSTEM` (brainstem)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
