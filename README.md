# Zypher — Enterprise AI Coding Assistant

**Zypher Brain** is the permanent source of knowledge. The language model is a **replaceable reasoning engine** only.

Add new documents to `knowledge-base/` anytime — no model retraining required.

## Architecture

```
User Message
      │
      ▼
┌─────────────────────────────────────────────────────────────────┐
│                        ZYPHER BRAIN                             │
│  Knowledge Base · Vector DB · Metadata · Graph · Memory          │
│                                                                 │
│  1. Save conversation                                           │
│  2. Embed query                                                 │
│  3. Vector search                                               │
│  4. Metadata filter search                                      │
│  5. Graph relationship traversal                                │
│  6. Merge + re-rank                                             │
│  7. Build context window                                        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   LLM (Reasoning Engine)                        │
│  poolside/Laguna-XS-2.1 · optional adapter · swappable          │
│  Answers ONLY from Zypher Brain context                         │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
                      Final Answer
```

| Component | Role |
|-----------|------|
| **Zypher Brain** | Primary knowledge — docs, APIs, code, ADRs, runbooks, SQL |
| **LLM** | Reasoning over retrieved context (not internal knowledge) |
| **Optional fine-tune** | Style/domain tuning — not required for knowledge |

## Zypher Platform (complete stack)

Mega brain + enterprise platform layer:

```
                    ┌─────────────────────────────────┐
                    │       Zypher Platform API       │
                    │  REST · Sessions · Jobs · Admin │
                    └───────────────┬─────────────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          ▼                         ▼                         ▼
   ┌─────────────┐          ┌─────────────┐          ┌─────────────┐
   │ Zypher Brain│          │  LLM Engine │          │   Agents    │
   │  (knowledge)│          │ (reasoning) │          │ (tools/RAG) │
   └─────────────┘          └─────────────┘          └─────────────┘
```

```bash
make generate-mega      # expand brain
make platform-index     # index brain
make serve              # REST API on :8080
```

### API endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/v1/stats` | GET | Brain + platform statistics |
| `/v1/chat` | POST | Chat with brain retrieval + LLM |
| `/v1/retrieve` | POST | Search brain only (no LLM) |
| `/v1/documents` | POST | Ingest new doc (no retraining) |
| `/v1/index` | POST | Enqueue index job |
| `/v1/generate` | POST | Enqueue mega corpus job |
| `/v1/sessions` | POST/GET | Conversation sessions |
| `/v1/jobs/{id}/run` | POST | Run background job |

### Platform module

```
zypher_platform/
├── core.py           # ZypherPlatform orchestrator
├── api/app.py        # FastAPI REST API
├── sessions/         # Multi-user conversation store
├── jobs/             # Background index + generate jobs
└── agents/           # Tool-calling agent orchestrator
```

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

make generate-smoke     # expand knowledge corpus (optional)
make index              # build Zypher Brain vector index
make chat               # Brain retrieval + LLM reasoning
```

No fine-tuning required. To enable an optional adapter, set `adapter.enabled: true` in `config/llm.yaml`.

## Zypher Product (value-first package)

The product package delivers **curated knowledge**, not just volume. It includes everything needed for production RAG:

| Component | What you get |
|-----------|--------------|
| Curated knowledge base | Original `CHUNK-*.md` documents with accurate metadata |
| Vector-ready chunks | `data/product/chunks/chunks.jsonl` |
| Embeddings | Pre-computed vectors + generation scripts |
| Graph relationships | Typed edges (`depends_on`, `uses`, `see_also`, …) |
| Metadata index | `data/product/metadata/documents.json` |
| Benchmark datasets | FAQ pairs, retrieval gold, RAG eval |
| Evaluation scripts | Recall@k, faithfulness, evidence report |
| Examples + docs | RAG pipeline, API client, setup guides |

```bash
make product      # Full build: chunks → dedup → validate → graph → embeddings → benchmarks
make evaluate     # Run evaluation + evidence report
```

> The biggest challenge isn't making it big — it's making it valuable.

Quality gates enforce: original content, accurate metadata, ≤5% duplication, clear Apache-2.0 licensing, and retrieval evidence.

See [docs/product-setup.md](docs/product-setup.md) for the full guide.

## Zypher Brain module

```
brain/
├── brain.py              # ZypherBrain service
├── ingestion/            # Load markdown documents
├── embeddings/           # Query/document embeddings
├── indexing/             # ChromaDB vector index
├── metadata/             # doc_type, category, tag filters
├── graph/                # Typed relationship traversal
├── reranking/            # Merge + score results
├── retrieval/            # Full retrieval pipeline
└── memory/               # Conversation memory
```

### Knowledge types supported

Documentation · FAQs · API References · ADRs · Runbooks · Troubleshooting · Code Examples · SQL Examples · Deployment Guides · Incident Reports · Design Documents · Code Reviews

### Retrieval flow

1. Save conversation
2. Generate embedding for user query
3. Search vector database
4. Search metadata filters
5. Search graph relationships
6. Merge and re-rank results
7. Build context window
8. Send context to LLM
9. Return generated answer

## Configuration

| File | Purpose |
|------|---------|
| `config/brain.yaml` | Knowledge paths, retrieval, graph, memory |
| `config/brain_curated.yaml` | Curated product mode (CHUNK docs only) |
| `config/product.yaml` | Product build, quality gates, benchmarks |
| `config/llm.yaml` | LLM provider, model, optional adapter |
| `config/corpus_generation.yaml` | Corpus generator settings |

## Add knowledge (no retraining)

```bash
# 1. Add markdown to knowledge-base/
echo "# My Runbook\n..." > knowledge-base/my-runbook.md

# 2. Re-index
make index

# 3. Chat — Brain retrieves the new doc automatically
make chat
```

## Optional: corpus generation + fine-tuning

```bash
make generate-smoke
make prepare
make train-xs          # optional — enable adapter in config/llm.yaml
```

## Project structure

```
.
├── brain/                    # Zypher Brain (primary knowledge service)
├── zypher/                   # Chatbot CLI + LLM provider
│   ├── backend.py
│   ├── chat.py
│   └── llm/provider.py       # Swappable reasoning engine
├── knowledge-base/           # Seed + generated documents
├── data/product/             # Product artifacts (chunks, embeddings, graph)
├── benchmarks/               # Evaluation datasets + evidence reports
├── examples/                 # RAG query, API client examples
├── docs/                     # Setup, quality, evaluation, licensing guides
├── scripts/
│   ├── product/              # Product build pipeline
│   ├── generate_corpus.py    # Expand brain corpus
│   └── prepare_advanced_dataset.py  # Optional training data
└── config/
    ├── brain.yaml
    ├── brain_curated.yaml
    ├── product.yaml
    └── llm.yaml
```

## Future compatibility

- Multiple language models (swap in `config/llm.yaml`)
- Model swapping without touching Brain
- Optional fine-tuning (adapter path)
- GraphRAG typed relationships
- Tool calling (`search_zypher_brain`)
- Multi-agent workflows
- Enterprise deployments

## Scale the brain (mega)

| Command | Documents | Where to run |
|---------|-----------|--------------|
| `make generate-smoke` | 2,000 | Local |
| `make generate` | ~112,000 | Local / cloud |
| `make generate-mega` | 100,000 | Vast.ai |
| `make generate-ultra` | 1,000,000 | Vast.ai |
| `make generate-hyper` | Billions (uncapped) | Vast.ai cluster |

Hyper tier uses `mega_multiplier: 100000000000` — procedural streaming, no memory limit.

```bash
# On Vast.ai — mega brain
make generate-mega && make index && make chat

# Full hyper (100B× tier — billions of docs)
make generate-hyper
```

Check stats: `cat knowledge-base/generated/brain_statistics.json`

## Hardware

| Step | GPU | Notes |
|------|-----|-------|
| `make index` | CPU OK | Embeddings via sentence-transformers |
| `make chat` | 24 GB+ VRAM | 4-bit LLM inference |
| `make train-xs` | Optional | Not required for knowledge |
