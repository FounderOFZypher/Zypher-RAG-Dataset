---
id: CHUNK-02108-API-CONTRACT-TESTING-WITH-PACT-BENCHMARK-V404
title: "Chunk 02108 API Contract Testing with Pact \u2014 Benchmark (v404)"
category: CHUNK-02108-api_contract_testing_with_pact_benchmark_v404.md
tags:
- pact
- contracts
- consumer
- provider
- benchmark
- testing
- variant_404
difficulty: intermediate
related:
- CHUNK-02107
- CHUNK-02106
- CHUNK-02105
last_updated: '2026-07-07'
version: '2.0'
---

---
id: CHUNK-02108
title: "API Contract Testing with Pact \u2014 Benchmark (v404)"
category: testing
doc_type: benchmark
tags:
- pact
- contracts
- consumer
- provider
- benchmark
- testing
- variant_404
difficulty: intermediate
related: []
last_updated: '2026-07-07'
version: '2.0'
hub: domain_testing
---

# API Contract Testing with Pact — Benchmark (v404)

## Suite

Under high load, **Suite** for `API Contract Testing with Pact` (benchmark). This variant 404 covers pact, contracts, consumer, provider at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Methodology

Under high load, **Methodology** for `API Contract Testing with Pact` (benchmark). This variant 404 covers pact, contracts, consumer, provider at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Dataset

Under high load, **Dataset** for `API Contract Testing with Pact` (benchmark). This variant 404 covers pact, contracts, consumer, provider at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Metrics

**Metrics** — API Contract Testing with Pact benchmark variant 404.

| Metric | Value |
|--------|-------|
| recall@10 | 0.80 |
| p95 latency (ms) | 6180 |
| error rate | 0.4050 |

**Good answer:** Grounded in measured results with trade-offs.
**Bad answer:** Claims without metrics or missing failure modes.
**Preferred answer:** Cites numbers, context, and next optimization steps.
## Results

**Results** — API Contract Testing with Pact benchmark variant 404.

| Metric | Value |
|--------|-------|
| recall@10 | 0.80 |
| p95 latency (ms) | 6180 |
| error rate | 0.4050 |

**Good answer:** Grounded in measured results with trade-offs.
**Bad answer:** Claims without metrics or missing failure modes.
**Preferred answer:** Cites numbers, context, and next optimization steps.
## Comparison

Under high load, **Comparison** for `API Contract Testing with Pact` (benchmark). This variant 404 covers pact, contracts, consumer, provider at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Reference Implementation

```typescript
interface ContractTestingConfig {
  topic: string;
  variant: number;
}

export async function handleContractTesting(config: ContractTestingConfig): Promise<Record<string, unknown>> {
  return { status: "ok", topic: config.topic, variant: config.variant };
}
```
