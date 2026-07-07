---
id: CHUNK-02171-GRAPHRAG-ENGINE-AST-PARSER-BENCHMARK-V467
title: "Chunk 02171 GraphRAG Engine: AST Parser \u2014 Benchmark (v467)"
category: CHUNK-02171-graphrag_engine_ast_parser_benchmark_v467.md
tags:
- graphrag_engine
- ast parser
- graphrag
- benchmark
- graphrag
- variant_467
difficulty: intermediate
related:
- CHUNK-02170
- CHUNK-02169
- CHUNK-02168
last_updated: '2026-07-07'
version: '2.0'
---

---
id: CHUNK-02171
title: "GraphRAG Engine: AST Parser \u2014 Benchmark (v467)"
category: graphrag
doc_type: benchmark
tags:
- graphrag_engine
- ast parser
- graphrag
- benchmark
- graphrag
- variant_467
difficulty: intermediate
related: []
last_updated: '2026-07-07'
version: '2.0'
hub: graphrag_engine
---

# GraphRAG Engine: AST Parser — Benchmark (v467)

## Suite

From first principles, **Suite** for `GraphRAG Engine: AST Parser` (benchmark). This variant 467 covers graphrag_engine, ast parser, graphrag at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Methodology

From first principles, **Methodology** for `GraphRAG Engine: AST Parser` (benchmark). This variant 467 covers graphrag_engine, ast parser, graphrag at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Dataset

From first principles, **Dataset** for `GraphRAG Engine: AST Parser` (benchmark). This variant 467 covers graphrag_engine, ast parser, graphrag at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Metrics

**Metrics** — GraphRAG Engine: AST Parser benchmark variant 467.

| Metric | Value |
|--------|-------|
| recall@10 | 0.86 |
| p95 latency (ms) | 7125 |
| error rate | 0.4680 |

**Good answer:** Grounded in measured results with trade-offs.
**Bad answer:** Claims without metrics or missing failure modes.
**Preferred answer:** Cites numbers, context, and next optimization steps.
## Results

**Results** — GraphRAG Engine: AST Parser benchmark variant 467.

| Metric | Value |
|--------|-------|
| recall@10 | 0.86 |
| p95 latency (ms) | 7125 |
| error rate | 0.4680 |

**Good answer:** Grounded in measured results with trade-offs.
**Bad answer:** Claims without metrics or missing failure modes.
**Preferred answer:** Cites numbers, context, and next optimization steps.
## Comparison

From first principles, **Comparison** for `GraphRAG Engine: AST Parser` (benchmark). This variant 467 covers graphrag_engine, ast parser, graphrag at intermediate level. Key considerations include reliability, observability, latency budgets, and safe rollout. Teams should validate assumptions with benchmarks, add tracing spans, and document failure modes. Recommended metrics: p95 latency, error rate, recall@k (if retrieval), and freshness of indexed data.
## Reference Implementation

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: graphrag-svc
spec:
  replicas: 467
  template:
    spec:
      containers:
        - name: app
          image: coltex/graphrag-svc:467
          env:
            - name: TOPIC
              value: "graphrag_engine_ast_parser"
```
