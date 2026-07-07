---
id: PATHWAY-0501
title: "Domain Pathway: cerebellum → temporal (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: cerebellum
lobe_target: temporal
pathway_type: inhibitory
tags: [pathway, inhibitory, cerebellum, temporal]
related: [LOBE-CEREBELLUM, LOBE-TEMPORAL]
see_also: [LOBE-CEREBELLUM, LOBE-TEMPORAL]
synthesizes: [LOBE-CEREBELLUM]
---

# Domain Pathway: cerebellum → temporal

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `cerebellum` connect to lobe `temporal` via this commissural pathway.

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
- Target: `LOBE-TEMPORAL` (temporal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
