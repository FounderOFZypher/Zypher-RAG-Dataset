---
id: PATHWAY-0709
title: "Domain Pathway: hippocampus → amygdala (inhibitory)"
doc_type: neural_pathway
category: graphrag
hub: coltex_knowledge_core
lobe_source: hippocampus
lobe_target: amygdala
pathway_type: inhibitory
tags: [pathway, inhibitory, hippocampus, amygdala]
related: [LOBE-HIPPOCAMPUS, LOBE-AMYGDALA]
see_also: [LOBE-HIPPOCAMPUS, LOBE-AMYGDALA]
synthesizes: [LOBE-HIPPOCAMPUS]
---

# Domain Pathway: hippocampus → amygdala

**Type:** `inhibitory` · **Tier:** association layer

## Route
Documents in lobe `hippocampus` connect to lobe `amygdala` via this commissural pathway.

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
- Target: `LOBE-AMYGDALA` (amygdala)

## Coltex Knowledge Architecture
Advanced neural routing (`NeuralRouter`) boosts documents in `/pathways/` during GraphRAG expansion.
