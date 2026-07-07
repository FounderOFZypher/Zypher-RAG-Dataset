---
id: PATHWAY-0605
title: "Domain Pathway: brainstem → cerebellum (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: brainstem
lobe_target: cerebellum
pathway_type: inhibitory
tags: [pathway, inhibitory, brainstem, cerebellum]
related: [LOBE-BRAINSTEM, LOBE-CEREBELLUM]
see_also: [LOBE-BRAINSTEM, LOBE-CEREBELLUM]
synthesizes: [LOBE-BRAINSTEM]
---

# Domain Pathway: brainstem → cerebellum

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `brainstem` connect to lobe `cerebellum` via this commissural pathway.

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
- Target: `LOBE-CEREBELLUM` (cerebellum)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
