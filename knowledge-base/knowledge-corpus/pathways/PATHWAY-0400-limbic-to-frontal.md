---
id: PATHWAY-0400
title: "Domain Pathway: limbic → frontal (commissural)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: limbic
lobe_target: frontal
pathway_type: commissural
tags: [pathway, commissural, limbic, frontal]
related: [LOBE-LIMBIC, LOBE-FRONTAL]
see_also: [LOBE-LIMBIC, LOBE-FRONTAL]
synthesizes: [LOBE-LIMBIC]
---

# Domain Pathway: limbic → frontal

**Type:** `commissural` · **Tier:** association layer

## Route
Documents in lobe `limbic` connect to lobe `frontal` via this commissural pathway.

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
- Target: `LOBE-FRONTAL` (frontal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
