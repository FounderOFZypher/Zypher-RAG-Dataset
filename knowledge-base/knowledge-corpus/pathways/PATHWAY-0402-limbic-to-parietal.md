---
id: PATHWAY-0402
title: "Domain Pathway: limbic → parietal (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: limbic
lobe_target: parietal
pathway_type: inhibitory
tags: [pathway, inhibitory, limbic, parietal]
related: [LOBE-LIMBIC, LOBE-PARIETAL]
see_also: [LOBE-LIMBIC, LOBE-PARIETAL]
synthesizes: [LOBE-LIMBIC]
---

# Domain Pathway: limbic → parietal

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `limbic` connect to lobe `parietal` via this commissural pathway.

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
- Target: `LOBE-PARIETAL` (parietal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
