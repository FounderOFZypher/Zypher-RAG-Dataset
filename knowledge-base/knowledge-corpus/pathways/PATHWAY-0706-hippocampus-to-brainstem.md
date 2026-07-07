---
id: PATHWAY-0706
title: "Domain Pathway: hippocampus → brainstem (associative)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: hippocampus
lobe_target: brainstem
pathway_type: associative
tags: [pathway, associative, hippocampus, brainstem]
related: [LOBE-HIPPOCAMPUS, LOBE-BRAINSTEM]
see_also: [LOBE-HIPPOCAMPUS, LOBE-BRAINSTEM]
synthesizes: [LOBE-HIPPOCAMPUS]
---

# Domain Pathway: hippocampus → brainstem

**Type:** `associative` · **Tier:** association layer

## Route
Documents in lobe `hippocampus` connect to lobe `brainstem` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-HIPPOCAMPUS` (hippocampus)
- Target: `LOBE-BRAINSTEM` (brainstem)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
