---
id: PATHWAY-0205
title: "Domain Pathway: parietal → cerebellum (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: parietal
lobe_target: cerebellum
pathway_type: modulatory
tags: [pathway, modulatory, parietal, cerebellum]
related: [LOBE-PARIETAL, LOBE-CEREBELLUM]
see_also: [LOBE-PARIETAL, LOBE-CEREBELLUM]
synthesizes: [LOBE-PARIETAL]
---

# Domain Pathway: parietal → cerebellum

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `parietal` connect to lobe `cerebellum` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-PARIETAL` (parietal)
- Target: `LOBE-CEREBELLUM` (cerebellum)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
