---
id: PATHWAY-0907
title: "Domain Pathway: amygdala → hippocampus (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: amygdala
lobe_target: hippocampus
pathway_type: inhibitory
tags: [pathway, inhibitory, amygdala, hippocampus]
related: [LOBE-AMYGDALA, LOBE-HIPPOCAMPUS]
see_also: [LOBE-AMYGDALA, LOBE-HIPPOCAMPUS]
synthesizes: [LOBE-AMYGDALA]
---

# Domain Pathway: amygdala → hippocampus

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `amygdala` connect to lobe `hippocampus` via this commissural pathway.

## Traversal weight
| Pathway type | Graph boost |
|--------------|-------------|
| excitatory | +15% retrieval score |
| inhibitory | suppresses conflicts |
| modulatory | adjusts rerank |
| associative | default cross-link |
| commissural | inter-lobe bridge |

## Anchors
- Source: `LOBE-AMYGDALA` (amygdala)
- Target: `LOBE-HIPPOCAMPUS` (hippocampus)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
