---
id: PATHWAY-0703
title: "Domain Pathway: hippocampus → occipital (excitatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: hippocampus
lobe_target: occipital
pathway_type: excitatory
tags: [pathway, excitatory, hippocampus, occipital]
related: [LOBE-HIPPOCAMPUS, LOBE-OCCIPITAL]
see_also: [LOBE-HIPPOCAMPUS, LOBE-OCCIPITAL]
synthesizes: [LOBE-HIPPOCAMPUS]
---

# Domain Pathway: hippocampus → occipital

**Type:** `excitatory` · **Tier:** association layer

## Route
Documents in lobe `hippocampus` connect to lobe `occipital` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-HIPPOCAMPUS` (hippocampus)
- Target: `LOBE-OCCIPITAL` (occipital)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
