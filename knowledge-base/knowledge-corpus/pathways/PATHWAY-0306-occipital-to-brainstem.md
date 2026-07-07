---
id: PATHWAY-0306
title: "Domain Pathway: occipital → brainstem (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: occipital
lobe_target: brainstem
pathway_type: commissural
tags: [pathway, commissural, occipital, brainstem]
related: [LOBE-OCCIPITAL, LOBE-BRAINSTEM]
see_also: [LOBE-OCCIPITAL, LOBE-BRAINSTEM]
synthesizes: [LOBE-OCCIPITAL]
---

# Domain Pathway: occipital → brainstem

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `occipital` connect to lobe `brainstem` via this commissural pathway.

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
- Target: `LOBE-BRAINSTEM` (brainstem)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
