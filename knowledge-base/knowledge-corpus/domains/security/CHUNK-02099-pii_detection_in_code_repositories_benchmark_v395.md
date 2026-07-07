---
id: CHUNK-02099-PII-DETECTION-IN-CODE-REPOSITORIES-BENCHMARK-V395
title: "Chunk 02099 PII Detection in Code Repositories \u2014 Benchmark (v395)"
category: CHUNK-02099-pii_detection_in_code_repositories_benchmark_v395.md
tags:
- pii
- redaction
- scanning
- compliance
- benchmark
- security
- variant_395
difficulty: advanced
related:
- CHUNK-02098
- CHUNK-02097
- CHUNK-02096
last_updated: '2026-07-07'
version: '2.0'
---

---
id: CHUNK-02099
title: "PII Detection in Code Repositories \u2014 Benchmark (v395)"
category: security
doc_type: benchmark
tags:
- pii
- redaction
- scanning
- compliance
- benchmark
- security
- variant_395
difficulty: advanced
related: []
last_updated: '2026-07-07'
version: '2.0'
hub: domain_security
---

# PII Detection in Code Repositories — Benchmark (v395)

## Suite

From first principles, **Suite** for `PII Detection in Code Repositories` (benchmark). This variant 395 covers pii, redaction, scanning, compliance at advanced level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Methodology

From first principles, **Methodology** for `PII Detection in Code Repositories` (benchmark). This variant 395 covers pii, redaction, scanning, compliance at advanced level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Dataset

From first principles, **Dataset** for `PII Detection in Code Repositories` (benchmark). This variant 395 covers pii, redaction, scanning, compliance at advanced level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Metrics

**Metrics** — PII Detection in Code Repositories benchmark variant 395.

| Metric | Value |
|--------|-------|
| recall@10 | 0.82 |
| p95 latency (ms) | 6045 |
| error rate | 0.3960 |

**Good answer:** Grounded in measured results with trade-offs.
**Bad answer:** Claims without metrics or missing failure modes.
**Preferred answer:** Cites numbers, context, and next optimization steps.
## Results

**Results** — PII Detection in Code Repositories benchmark variant 395.

| Metric | Value |
|--------|-------|
| recall@10 | 0.82 |
| p95 latency (ms) | 6045 |
| error rate | 0.3960 |

**Good answer:** Grounded in measured results with trade-offs.
**Bad answer:** Claims without metrics or missing failure modes.
**Preferred answer:** Cites numbers, context, and next optimization steps.
## Comparison

From first principles, **Comparison** for `PII Detection in Code Repositories` (benchmark). This variant 395 covers pii, redaction, scanning, compliance at advanced level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Reference Implementation

```sql
CREATE TABLE IF NOT EXISTS security_395 (
    id          BIGSERIAL PRIMARY KEY,
    topic       TEXT NOT NULL,
    variant     INTEGER NOT NULL DEFAULT 395,
    payload     JSONB NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_security_395_topic ON security_395 (topic);

EXPLAIN ANALYZE
SELECT id, topic, payload FROM security_395
WHERE topic = 'pii_detection' ORDER BY created_at DESC LIMIT 50;
```
