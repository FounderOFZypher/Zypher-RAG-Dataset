---
id: PATHWAY-0006
title: "Domain Pathway: frontal → brainstem (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: frontal
lobe_target: brainstem
pathway_type: inhibitory
tags: [pathway, inhibitory, frontal, brainstem]
related: [LOBE-FRONTAL, LOBE-BRAINSTEM]
see_also: [LOBE-FRONTAL, LOBE-BRAINSTEM]
synthesizes: [LOBE-FRONTAL]
---

# Domain Pathway: frontal → brainstem

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `frontal` connect to lobe `brainstem` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-FRONTAL` (frontal)
- Target: `LOBE-BRAINSTEM` (brainstem)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
