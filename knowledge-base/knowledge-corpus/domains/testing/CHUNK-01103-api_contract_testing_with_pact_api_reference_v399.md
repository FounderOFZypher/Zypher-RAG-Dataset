---
id: CHUNK-01103-API-CONTRACT-TESTING-WITH-PACT-API-REFERENCE-V399
title: "Chunk 01103 API Contract Testing with Pact \u2014 Api Reference (v399)"
category: CHUNK-01103-api_contract_testing_with_pact_api_reference_v399.md
tags:
- pact
- contracts
- consumer
- provider
- api_reference
- testing
- variant_399
difficulty: intermediate
related:
- CHUNK-01102
- CHUNK-01101
- CHUNK-01100
last_updated: '2026-07-07'
version: '2.0'
---

---
id: CHUNK-01103
title: "API Contract Testing with Pact \u2014 Api Reference (v399)"
category: testing
doc_type: api_reference
tags:
- pact
- contracts
- consumer
- provider
- api_reference
- testing
- variant_399
difficulty: intermediate
related: []
last_updated: '2026-07-07'
version: '2.0'
hub: domain_testing
---

# API Contract Testing with Pact — Api Reference (v399)

## Endpoint

When integrating with legacy systems, **Endpoint** for `API Contract Testing with Pact` (api_reference). This variant 399 covers pact, contracts, consumer, provider at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Authentication

When integrating with legacy systems, **Authentication** for `API Contract Testing with Pact` (api_reference). This variant 399 covers pact, contracts, consumer, provider at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Request Schema

When integrating with legacy systems, **Request Schema** for `API Contract Testing with Pact` (api_reference). This variant 399 covers pact, contracts, consumer, provider at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Response Schema

When integrating with legacy systems, **Response Schema** for `API Contract Testing with Pact` (api_reference). This variant 399 covers pact, contracts, consumer, provider at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Error Codes

When integrating with legacy systems, **Error Codes** for `API Contract Testing with Pact` (api_reference). This variant 399 covers pact, contracts, consumer, provider at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Reference Implementation

```sql
CREATE TABLE IF NOT EXISTS testing_399 (
    id          BIGSERIAL PRIMARY KEY,
    topic       TEXT NOT NULL,
    variant     INTEGER NOT NULL DEFAULT 399,
    payload     JSONB NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_testing_399_topic ON testing_399 (topic);

EXPLAIN ANALYZE
SELECT id, topic, payload FROM testing_399
WHERE topic = 'contract_testing' ORDER BY created_at DESC LIMIT 50;
```
