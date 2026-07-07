---
id: PATHWAY-0607
title: "Domain Pathway: brainstem → hippocampus (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: brainstem
lobe_target: hippocampus
pathway_type: associative
tags: [pathway, associative, brainstem, hippocampus]
related: [LOBE-BRAINSTEM, LOBE-HIPPOCAMPUS]
see_also: [LOBE-BRAINSTEM, LOBE-HIPPOCAMPUS]
synthesizes: [LOBE-BRAINSTEM]
---

# Domain Pathway: brainstem → hippocampus

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `brainstem` connect to lobe `hippocampus` via this commissural pathway.

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
- Target: `LOBE-HIPPOCAMPUS` (hippocampus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
