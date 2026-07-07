---
id: SYNAPSE-00068
title: "Synapse: payment_service ↔ incident_command"
doc_type: deep_dive
category: graphrag
hub: coltex_knowledge_core
tags: [synapse, graph, payment_service, incident_command]
related: [HUB-PAYMENT_SERVICE, HUB-INCIDENT_COMMAND]
see_also: [HUB-PAYMENT_SERVICE, HUB-INCIDENT_COMMAND]
depends_on: [HUB-PAYMENT_SERVICE]
---

# Cross-Reference Link: payment_service → incident_command

Cross-domain connection in the Coltex Knowledge Corpus graph.

## Connection type
**see_also** — documents in `payment_service` is related to `incident_command`.

## Source hub
- Hub: `payment_service`
- Anchor: `HUB-PAYMENT_SERVICE`

## Target hub
- Hub: `incident_command`
- Anchor: `HUB-INCIDENT_COMMAND`

## Traversal hint
When querying either domain, GraphRAG expansion follows this synapse for multi-hop context.

## Coltex brain note
Synapses are first-class graph edges. The retrieval pipeline uses `see_also` and `depends_on`
to surface related knowledge across domain boundaries.
