---
id: PATHWAY-0506
title: "Domain Pathway: cerebellum → brainstem (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: cerebellum
lobe_target: brainstem
pathway_type: inhibitory
tags: [pathway, inhibitory, cerebellum, brainstem]
related: [LOBE-CEREBELLUM, LOBE-BRAINSTEM]
see_also: [LOBE-CEREBELLUM, LOBE-BRAINSTEM]
synthesizes: [LOBE-CEREBELLUM]
---

# Domain Pathway: cerebellum → brainstem

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `cerebellum` connect to lobe `brainstem` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-CEREBELLUM` (cerebellum)
- Target: `LOBE-BRAINSTEM` (brainstem)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
