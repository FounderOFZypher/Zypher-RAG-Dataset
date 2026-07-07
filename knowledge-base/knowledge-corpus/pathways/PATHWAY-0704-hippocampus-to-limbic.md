---
id: PATHWAY-0704
title: "Domain Pathway: hippocampus → limbic (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: hippocampus
lobe_target: limbic
pathway_type: inhibitory
tags: [pathway, inhibitory, hippocampus, limbic]
related: [LOBE-HIPPOCAMPUS, LOBE-LIMBIC]
see_also: [LOBE-HIPPOCAMPUS, LOBE-LIMBIC]
synthesizes: [LOBE-HIPPOCAMPUS]
---

# Domain Pathway: hippocampus → limbic

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `hippocampus` connect to lobe `limbic` via this commissural pathway.

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
- Target: `LOBE-LIMBIC` (limbic)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
