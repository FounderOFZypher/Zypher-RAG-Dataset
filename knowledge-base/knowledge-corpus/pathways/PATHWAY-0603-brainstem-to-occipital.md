---
id: PATHWAY-0603
title: "Domain Pathway: brainstem → occipital (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: brainstem
lobe_target: occipital
pathway_type: commissural
tags: [pathway, commissural, brainstem, occipital]
related: [LOBE-BRAINSTEM, LOBE-OCCIPITAL]
see_also: [LOBE-BRAINSTEM, LOBE-OCCIPITAL]
synthesizes: [LOBE-BRAINSTEM]
---

# Domain Pathway: brainstem → occipital

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `brainstem` connect to lobe `occipital` via this commissural pathway.

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
- Target: `LOBE-OCCIPITAL` (occipital)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
