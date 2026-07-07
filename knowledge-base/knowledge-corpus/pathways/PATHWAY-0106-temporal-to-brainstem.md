---
id: PATHWAY-0106
title: "Domain Pathway: temporal → brainstem (modulatory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: temporal
lobe_target: brainstem
pathway_type: modulatory
tags: [pathway, modulatory, temporal, brainstem]
related: [LOBE-TEMPORAL, LOBE-BRAINSTEM]
see_also: [LOBE-TEMPORAL, LOBE-BRAINSTEM]
synthesizes: [LOBE-TEMPORAL]
---

# Domain Pathway: temporal → brainstem

**Type:** `modulatory` · **Tier:** association layer

## Route
Documents in lobe `temporal` connect to lobe `brainstem` via this commissural pathway.

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
- Target: `LOBE-BRAINSTEM` (brainstem)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
