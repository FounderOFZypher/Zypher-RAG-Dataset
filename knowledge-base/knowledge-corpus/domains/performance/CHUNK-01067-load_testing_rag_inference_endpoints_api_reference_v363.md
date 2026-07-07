---
id: CHUNK-01067-LOAD-TESTING-RAG-INFERENCE-ENDPOINTS-API-REFERENCE-V363
title: "Chunk 01067 Load Testing RAG Inference Endpoints \u2014 Api Reference (v363)"
category: CHUNK-01067-load_testing_rag_inference_endpoints_api_reference_v363.md
tags:
- k6
- locust
- throughput
- latency
- api_reference
- performance
- variant_363
difficulty: intermediate
related:
- CHUNK-01066
- CHUNK-01065
- CHUNK-01064
last_updated: '2026-07-07'
version: '2.0'
---

---
id: CHUNK-01067
title: "Load Testing RAG Inference Endpoints \u2014 Api Reference (v363)"
category: performance
doc_type: api_reference
tags:
- k6
- locust
- throughput
- latency
- api_reference
- performance
- variant_363
difficulty: intermediate
related: []
last_updated: '2026-07-07'
version: '2.0'
hub: domain_performance
---

# Load Testing RAG Inference Endpoints — Api Reference (v363)

## Endpoint

From first principles, **Endpoint** for `Load Testing RAG Inference Endpoints` (api_reference). This variant 363 covers k6, locust, throughput, latency at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Authentication

From first principles, **Authentication** for `Load Testing RAG Inference Endpoints` (api_reference). This variant 363 covers k6, locust, throughput, latency at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Request Schema

From first principles, **Request Schema** for `Load Testing RAG Inference Endpoints` (api_reference). This variant 363 covers k6, locust, throughput, latency at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Response Schema

From first principles, **Response Schema** for `Load Testing RAG Inference Endpoints` (api_reference). This variant 363 covers k6, locust, throughput, latency at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Error Codes

From first principles, **Error Codes** for `Load Testing RAG Inference Endpoints` (api_reference). This variant 363 covers k6, locust, throughput, latency at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Reference Implementation

```sql
CREATE TABLE IF NOT EXISTS performance_363 (
    id          BIGSERIAL PRIMARY KEY,
    topic       TEXT NOT NULL,
    variant     INTEGER NOT NULL DEFAULT 363,
    payload     JSONB NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_performance_363_topic ON performance_363 (topic);

EXPLAIN ANALYZE
SELECT id, topic, payload FROM performance_363
WHERE topic = 'load_testing' ORDER BY created_at DESC LIMIT 50;
```
