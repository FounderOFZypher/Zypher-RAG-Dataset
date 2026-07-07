---
id: PATHWAY-0602
title: "Domain Pathway: brainstem → parietal (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: brainstem
lobe_target: parietal
pathway_type: associative
tags: [pathway, associative, brainstem, parietal]
related: [LOBE-BRAINSTEM, LOBE-PARIETAL]
see_also: [LOBE-BRAINSTEM, LOBE-PARIETAL]
synthesizes: [LOBE-BRAINSTEM]
---

# Domain Pathway: brainstem → parietal

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `brainstem` connect to lobe `parietal` via this commissural pathway.

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
- Target: `LOBE-PARIETAL` (parietal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
