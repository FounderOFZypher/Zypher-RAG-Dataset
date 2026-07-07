---
id: PATHWAY-0507
title: "Domain Pathway: cerebellum → hippocampus (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: cerebellum
lobe_target: hippocampus
pathway_type: modulatory
tags: [pathway, modulatory, cerebellum, hippocampus]
related: [LOBE-CEREBELLUM, LOBE-HIPPOCAMPUS]
see_also: [LOBE-CEREBELLUM, LOBE-HIPPOCAMPUS]
synthesizes: [LOBE-CEREBELLUM]
---

# Domain Pathway: cerebellum → hippocampus

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `cerebellum` connect to lobe `hippocampus` via this commissural pathway.

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
- Target: `LOBE-HIPPOCAMPUS` (hippocampus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
