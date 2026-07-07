---
id: PATHWAY-0601
title: "Domain Pathway: brainstem → temporal (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: brainstem
lobe_target: temporal
pathway_type: modulatory
tags: [pathway, modulatory, brainstem, temporal]
related: [LOBE-BRAINSTEM, LOBE-TEMPORAL]
see_also: [LOBE-BRAINSTEM, LOBE-TEMPORAL]
synthesizes: [LOBE-BRAINSTEM]
---

# Domain Pathway: brainstem → temporal

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `brainstem` connect to lobe `temporal` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-BRAINSTEM` (brainstem)
- Target: `LOBE-TEMPORAL` (temporal)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
