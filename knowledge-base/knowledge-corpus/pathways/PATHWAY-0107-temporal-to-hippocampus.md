---
id: PATHWAY-0107
title: "Domain Pathway: temporal → hippocampus (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: temporal
lobe_target: hippocampus
pathway_type: associative
tags: [pathway, associative, temporal, hippocampus]
related: [LOBE-TEMPORAL, LOBE-HIPPOCAMPUS]
see_also: [LOBE-TEMPORAL, LOBE-HIPPOCAMPUS]
synthesizes: [LOBE-TEMPORAL]
---

# Domain Pathway: temporal → hippocampus

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `temporal` connect to lobe `hippocampus` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-TEMPORAL` (temporal)
- Target: `LOBE-HIPPOCAMPUS` (hippocampus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
