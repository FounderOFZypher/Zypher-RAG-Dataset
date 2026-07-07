---
id: PATHWAY-0407
title: "Domain Pathway: limbic → hippocampus (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: limbic
lobe_target: hippocampus
pathway_type: inhibitory
tags: [pathway, inhibitory, limbic, hippocampus]
related: [LOBE-LIMBIC, LOBE-HIPPOCAMPUS]
see_also: [LOBE-LIMBIC, LOBE-HIPPOCAMPUS]
synthesizes: [LOBE-LIMBIC]
---

# Domain Pathway: limbic → hippocampus

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `limbic` connect to lobe `hippocampus` via this commissural pathway.

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
- Target: `LOBE-HIPPOCAMPUS` (hippocampus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
