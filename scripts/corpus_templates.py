"""Topic and template definitions for scalable knowledge-base generation."""

from __future__ import annotations

from dataclasses import dataclass

CATEGORIES = [
    "rag",
    "graphrag",
    "agentic",
    "chunking",
    "embeddings",
    "vector_stores",
    "retrieval",
    "indexing",
    "security",
    "observability",
    "kubernetes",
    "api_design",
    "python",
    "typescript",
    "rust",
    "go",
    "sql",
    "testing",
    "ci_cd",
    "architecture",
    "incidents",
    "code_review",
    "debugging",
    "performance",
    "data_quality",
    "mlops",
    "fine_tuning",
    "prompt_engineering",
    "tool_use",
    "memory",
]

DOCUMENT_TYPES = [
    "guide",
    "tutorial",
    "faq",
    "troubleshooting",
    "api_reference",
    "code_walkthrough",
    "architecture_decision",
    "runbook",
    "deep_dive",
    "comparison",
    "best_practices",
    "anti_patterns",
    "cheat_sheet",
    "interview_prep",
    "case_study",
]

ADVANCED_TASK_TYPES = [
    "single_turn_qa",
    "multi_turn_dialogue",
    "chain_of_thought",
    "tool_calling",
    "rag_with_context",
    "code_generation",
    "code_review",
    "debugging_session",
    "architecture_consultation",
    "incident_triage",
    "refactoring",
    "unit_test_generation",
    "api_design_review",
    "security_audit",
    "performance_analysis",
]


@dataclass(frozen=True)
class Topic:
    slug: str
    title: str
    category: str
    difficulty: str
    keywords: tuple[str, ...]


def _topics() -> list[Topic]:
    topics: list[Topic] = []
    seeds = [
        ("hybrid_search", "Hybrid Search with BM25 and Dense Retrieval", "retrieval", "advanced",
         ("bm25", "dense", "fusion", "reranking")),
        ("graph_traversal", "Graph Traversal for Dependency Analysis", "graphrag", "advanced",
         ("bfs", "dfs", "pagerank", "communities")),
        ("agent_memory", "Long-Horizon Agent Memory Systems", "agentic", "expert",
         ("episodic", "semantic", "working_memory", "summarization")),
        ("chunk_overlap", "Optimal Chunk Overlap Strategies", "chunking", "intermediate",
         ("overlap", "boundaries", "context", "sliding_window")),
        ("hnsw_tuning", "HNSW Index Parameter Tuning", "vector_stores", "advanced",
         ("hnsw", "ef_construction", "m", "recall")),
        ("rag_eval", "RAG Evaluation Frameworks", "rag", "advanced",
         ("faithfulness", "relevance", "ragas", "benchmarks")),
        ("tool_router", "Tool Routing in Agentic Pipelines", "tool_use", "expert",
         ("routing", "function_calling", "orchestration", "guardrails")),
        ("otel_tracing", "OpenTelemetry Tracing for LLM Apps", "observability", "intermediate",
         ("otel", "spans", "latency", "tracing")),
        ("k8s_hpa", "Kubernetes HPA for Inference Services", "kubernetes", "intermediate",
         ("hpa", "autoscaling", "gpu", "serving")),
        ("jwt_auth", "JWT Authentication for Internal APIs", "security", "intermediate",
         ("jwt", "oauth", "rbac", "tokens")),
        ("async_python", "Async Python for High-Throughput Pipelines", "python", "advanced",
         ("asyncio", "aiohttp", "concurrency", "queues")),
        ("ts_generics", "Advanced TypeScript Generics", "typescript", "advanced",
         ("generics", "utility_types", "inference", "constraints")),
        ("rust_ownership", "Rust Ownership in Systems Programming", "rust", "advanced",
         ("ownership", "borrowing", "lifetimes", "safety")),
        ("go_concurrency", "Go Concurrency Patterns", "go", "intermediate",
         ("goroutines", "channels", "select", "worker_pools")),
        ("sql_optimization", "SQL Query Optimization", "sql", "advanced",
         ("indexes", "explain", "joins", "partitioning")),
        ("property_testing", "Property-Based Testing Strategies", "testing", "advanced",
         ("hypothesis", "invariants", "fuzzing", "generators")),
        ("canary_deploy", "Canary Deployment Pipelines", "ci_cd", "intermediate",
         ("canary", "rollback", "feature_flags", "promotion")),
        ("event_sourcing", "Event Sourcing Architecture", "architecture", "expert",
         ("events", "cqrs", "projections", "sagas")),
        ("postmortem", "Blameless Postmortem Writing", "incidents", "intermediate",
         ("timeline", "root_cause", "action_items", "lessons")),
        ("pr_review", "High-Quality Pull Request Reviews", "code_review", "intermediate",
         ("feedback", "nits", "architecture", "tests")),
        ("perf_profiling", "CPU Profiling for Python Services", "performance", "advanced",
         ("cprofile", "flamegraphs", "bottlenecks", "optimization")),
        ("data_drift", "Detecting Data Drift in RAG Indexes", "data_quality", "advanced",
         ("drift", "monitoring", "freshness", "alerts")),
        ("model_registry", "ML Model Registry Patterns", "mlops", "intermediate",
         ("registry", "versioning", "promotion", "lineage")),
        ("lora_sft", "LoRA Supervised Fine-Tuning", "fine_tuning", "advanced",
         ("lora", "qlora", "peft", "sft")),
        ("cot_prompting", "Chain-of-Thought Prompt Engineering", "prompt_engineering", "advanced",
         ("cot", "reasoning", "scratchpad", "verification")),
    ]

    for slug, title, category, difficulty, keywords in seeds:
        topics.append(Topic(slug, title, category, difficulty, keywords))

    # Expand each category with numbered variants
    category_phrases = {
        "rag": "Retrieval-Augmented Generation",
        "graphrag": "GraphRAG",
        "agentic": "Agentic Workflows",
        "chunking": "Code Chunking",
        "embeddings": "Embedding Models",
        "vector_stores": "Vector Databases",
        "retrieval": "Information Retrieval",
        "indexing": "Document Indexing",
        "security": "Security Engineering",
        "observability": "Observability",
        "kubernetes": "Kubernetes Operations",
        "api_design": "API Design",
        "python": "Python Engineering",
        "typescript": "TypeScript Development",
        "rust": "Rust Systems",
        "go": "Go Microservices",
        "sql": "SQL and Databases",
        "testing": "Software Testing",
        "ci_cd": "CI/CD Pipelines",
        "architecture": "System Architecture",
        "incidents": "Incident Management",
        "code_review": "Code Review",
        "debugging": "Debugging",
        "performance": "Performance Engineering",
        "data_quality": "Data Quality",
        "mlops": "MLOps",
        "fine_tuning": "Model Fine-Tuning",
        "prompt_engineering": "Prompt Engineering",
        "tool_use": "LLM Tool Use",
        "memory": "Conversation Memory",
    }

    aspects = [
        "fundamentals", "patterns", "pitfalls", "scaling", "monitoring",
        "security", "testing", "migration", "integration", "optimization",
        "troubleshooting", "benchmarks", "cost_analysis", "team_workflows",
        "enterprise_rollout", "edge_cases", "versioning", "compliance",
        "disaster_recovery", "multi_tenant",
    ]

    for category, phrase in category_phrases.items():
        for i, aspect in enumerate(aspects):
            slug = f"{category}_{aspect}"
            title = f"{phrase}: {aspect.replace('_', ' ').title()}"
            difficulty = ["beginner", "intermediate", "advanced", "expert"][i % 4]
            keywords = (category, aspect, phrase.lower().split()[0])
            topics.append(Topic(slug, title, category, difficulty, keywords))

    return topics


TOPICS: list[Topic] = _topics()
