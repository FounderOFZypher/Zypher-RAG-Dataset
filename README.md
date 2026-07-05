# Zypher Training Data — Custom Chatbot & Advanced Fine-Tuning

Build your **own chatbot from scratch** — this repo ships a custom BPE tokenizer, decoder-only Transformer, and full training pipeline — or fine-tune a pretrained model on a large training corpus.

**Data clarification:** The seed knowledge base (`knowledge-base/`, ~167 manually curated files) is expanded by a corpus generator that **produces a large synthetic corpus from that structured seed**. At `SCALE=1000`, the generator creates ~112k templated documents across 30 categories; training examples (~650k–800k+) are derived from both seed and generated files via multi-task dataset preparation. This is **volume expansion through structured generation**, not 1000× more unique human-authored knowledge.

## What makes Zypher unique

Zypher is an **enterprise AI coding assistant** focused on production-grade code intelligence — not a general-purpose chatbot. Compared to generic LLM fine-tuning repos, this project is distinctive in several ways:

| Differentiator | Description |
|----------------|-------------|
| **Code-native RAG** | Knowledge spans RAG, GraphRAG, AST-based chunking, and retrieval APIs — designed for internal codebases, not open-web Q&A. |
| **GraphRAG reasoning** | Documents cover knowledge graphs, dependency traversal, and architectural reasoning over code structure. |
| **Agentic workflows** | Training data includes tool-calling patterns, multi-step debugging, incident triage, and human-in-the-loop flows. |
| **Enterprise operations** | Runbooks, ADRs, incident reports, support tickets, and security practices reflect real production constraints. |
| **Dual training paths** | Train a **from-scratch** model you fully own, or apply **LoRA/QLoRA** on Qwen/Llama using the same advanced dataset. |
| **Multi-task SFT** | One corpus produces 8+ task types: multi-turn dialogue, chain-of-thought, RAG-with-context, code review, and more. |
| **Structured seed → synthetic scale** | A curated seed corpus drives templated expansion, keeping domain focus while scaling training volume. |

## Architecture

```mermaid
flowchart TB
    subgraph Seed["Seed Knowledge Base (~167 curated files)"]
        KB["knowledge-base/<br/>CHUNK-*.md, schemas, OpenAPI, k8s configs"]
    end

    subgraph Generate["Corpus Generation"]
        GEN["scripts/generate_corpus.py"]
        SYN["knowledge-base/generated/<br/>~112k synthetic docs at SCALE=1000"]
    end

    subgraph Prepare["Dataset Preparation"]
        ADV["scripts/prepare_advanced_dataset.py"]
        JSONL["data/advanced/<br/>train.jsonl · val.jsonl · test.jsonl · pretrain.txt"]
    end

    subgraph Train["Training Paths"]
        direction TB
        SCRATCH["From-Scratch Path<br/>chatbot/cli.py"]
        TOK["BPE Tokenizer"]
        PT["Pretrain<br/>(next-token)"]
        SFT["SFT<br/>(chat JSONL)"]
        CHAT["Chat CLI"]

        HF["HuggingFace Path<br/>scripts/train.py"]
        LORA["QLoRA SFT<br/>Qwen / Llama"]
        INFER["scripts/infer.py"]
    end

  KB --> GEN
    GEN --> SYN
    KB --> ADV
    SYN --> ADV
    ADV --> JSONL

    JSONL --> TOK
    TOK --> PT
    PT --> SFT
    SFT --> CHAT

    JSONL --> LORA
    LORA --> INFER
```

## What's included

| Layer | Description |
|-------|-------------|
| **Seed corpus** | ~167 curated markdown chunks: RAG, GraphRAG, ADRs, code reviews, incidents, APIs |
| **Corpus generator** | Produces ~112k synthetic files from templates + seed at `SCALE=1000` |
| **Advanced dataset prep** | 8+ task types: multi-turn, chain-of-thought, tool calling, RAG, code gen/review |
| **From-scratch chatbot** | Custom BPE tokenizer + decoder-only Transformer + pretrain + SFT + chat CLI |
| **HF fine-tuning** | Optional LoRA/QLoRA path with Qwen/Llama base models |

## Project structure

```
.
├── chatbot/                      # Your from-scratch chatbot
│   ├── cli.py                    # train-tokenizer | pretrain | sft | chat
│   ├── model.py                  # Decoder-only Transformer (RoPE, SwiGLU, RMSNorm)
│   ├── tokenizer.py              # BPE tokenizer with chat special tokens
│   ├── dataset.py                # Pretrain + SFT datasets
│   ├── trainer.py                # Training loop
│   └── inference.py              # Chat inference engine
├── knowledge-base/               # Seed corpus (~167 curated files)
│   └── generated/                # Synthetic corpus (~112k files at scale=1000)
├── scripts/
│   ├── generate_corpus.py        # Synthetic corpus generator
│   ├── prepare_advanced_dataset.py  # Advanced multi-task JSONL builder
│   ├── prepare_dataset.py        # Simple prep (seed only)
│   ├── train.py                  # HuggingFace LoRA training
│   └── infer.py                  # HF inference
├── config/
│   ├── chatbot.yaml              # From-scratch model & training config
│   ├── corpus_generation.yaml    # Corpus scale & categories
│   └── training.yaml             # HuggingFace LoRA config
└── data/advanced/                # Generated training data (gitignored)
```

## Quick start — full pipeline

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 1. Generate synthetic corpus from seed (use generate-smoke for a quick test)
make generate              # SCALE=1000 → ~112k synthetic files
# make generate-smoke      # → 2,000 files

# 2. Build advanced training data
make prepare-advanced

# 3a. Train YOUR chatbot from scratch
make train-scratch
make chat

# 3b. OR fine-tune a pretrained model with LoRA
make train
```

## Corpus scale

The table below reflects **synthetic file count** and **derived training examples** (multiple task types per file). Seed files (~167) are included in training but not multiplied by `SCALE`.

| `SCALE` | Synthetic files | Training examples (approx.) |
|---------|-----------------|------------------------------|
| 10 | ~1,125 | ~8,000 |
| 100 | ~11,250 | ~80,000 |
| 1000 | ~112,500 | ~650,000–800,000+ |

```bash
SCALE=1000 make generate
python3 scripts/prepare_advanced_dataset.py
```

## Model architecture

The from-scratch chatbot (`chatbot/model.py`) is a **decoder-only causal Transformer** — the same family as GPT, Llama, and Qwen — implemented in PyTorch for full ownership and transparency.

### Default configuration (~85M parameters)

| Component | Setting | Role |
|-----------|---------|------|
| Token embedding | `vocab_size=32000` | Maps BPE tokens to `d_model` vectors |
| Positional encoding | RoPE (`rope_theta=10000`) | Relative position without fixed-length limits |
| Attention | 12 heads, causal mask | Self-attention over prior tokens only |
| Normalization | RMSNorm | Pre-norm stabilization (lighter than LayerNorm) |
| Feed-forward | SwiGLU (`d_ff=3072`) | Gated activation; better quality per parameter |
| Depth | 12 layers | Stack of attention + FFN blocks |
| Output head | Tied to embeddings | `lm_head` shares weights with token embedding |
| Context window | 2048 tokens | Configurable via `max_seq_len` |

### Tokenizer

- **BPE** (Byte-Pair Encoding) trained on the full corpus
- Chat special tokens: `<|user|>`, `<|assistant|>`, `<|system|>`, `<|tool|>`, `<|tool_result|>`, `<|think|>`, `<|/think|>`
- Format: `tokenizer.format_chat(messages)` → structured prompt for SFT and inference

### Training stages

1. **Tokenizer training** — learn BPE vocabulary from `knowledge-base/**/*.md`
2. **Pretrain** — next-token prediction on `data/advanced/pretrain.txt`
3. **SFT** — supervised fine-tuning on chat JSONL with multi-task examples
4. **Inference** — autoregressive generation with temperature + top-p sampling

Edit `config/chatbot.yaml` to scale `d_model`, `n_layers`, and `vocab_size` for larger models.

```bash
python3 -m chatbot.cli train-tokenizer --corpus-glob "knowledge-base/**/*.md"
python3 -m chatbot.cli pretrain --data data/advanced/pretrain.txt --max-steps 50000
python3 -m chatbot.cli sft --data data/advanced/train.jsonl --checkpoint outputs/pretrain/checkpoint-final
python3 -m chatbot.cli chat --checkpoint outputs/sft/checkpoint-final
```

## Advanced training task types

The advanced dataset builder creates multiple examples per knowledge file:

| Task type | Description |
|-----------|-------------|
| `faq` / `documentation` | Single-turn Q&A |
| `multi_turn_dialogue` | Follow-up conversations |
| `chain_of_thought` | Reasoning with `<|think|>` blocks |
| `tool_calling` | Simulated tool use with `<|tool|>` / `<|tool_result|>` |
| `rag_with_context` | Context-grounded answers |
| `code_generation` / `code_review` | Code tasks from walkthroughs |

## Benchmark goals

These are **target metrics** for evaluating models trained on this pipeline — not yet reported results from a completed training run.

### Language modeling (pretrain)

| Metric | Target | Notes |
|--------|--------|-------|
| Validation perplexity | < 15 | On held-out `pretrain.txt` split |
| Tokens/sec (A100) | > 20k | Default ~85M config, mixed precision |

### Chat quality (SFT)

| Metric | Target | Notes |
|--------|--------|-------|
| FAQ exact-match (seed set) | > 70% | On curated seed FAQ chunks only |
| RAG faithfulness | > 80% | Answer stays within provided context |
| Multi-turn coherence | > 75% | Human or LLM-judge rubric on 100-dialogue sample |

### Code tasks

| Metric | Target | Notes |
|--------|--------|-------|
| Code review relevance | > 70% | Review addresses stated issue |
| Syntax-valid generation | > 85% | Generated code parses without errors |

### Retrieval-augmented (Zypher domain)

| Metric | Target | Notes |
|--------|--------|-------|
| GraphRAG concept accuracy | > 75% | Correct use of graph/dependency terminology |
| ADR structure completeness | > 80% | Includes context, decision, consequences |

### Operational

| Metric | Target | Notes |
|--------|--------|-------|
| p95 inference latency (85M, GPU) | < 500 ms | 128-token prompt, 256-token output |
| Training reproducibility | ±2% val loss | Same seed, same hardware |

## Project roadmap

| Phase | Status | Deliverables |
|-------|--------|--------------|
| **v1.0 — Foundation** | Done | Seed corpus, corpus generator, advanced dataset prep, from-scratch chatbot stack |
| **v1.1 — Evaluation** | Planned | Benchmark scripts, automated eval on seed FAQ/RAG/code tasks |
| **v1.2 — RAG integration** | Planned | Retrieval index over seed KB, inference-time context injection |
| **v1.3 — Tool execution** | Planned | Live tool router (metrics, search, code lint) beyond simulated training examples |
| **v2.0 — Production model** | Planned | Larger default config (~350M–1B), distilled from pretrained teacher |
| **v2.1 — GraphRAG runtime** | Planned | Code graph builder + traversal API wired to chatbot inference |

## Limitations

Be aware of these constraints before training or deploying:

| Limitation | Impact |
|------------|--------|
| **Synthetic corpus dominance** | At full scale, most training text is templated — models may repeat phrasing patterns and lack depth on niche topics not in the seed. |
| **Small default model (~85M)** | Suitable for learning and prototyping; production quality typically requires larger models or the HF LoRA path with a 1.5B–7B base. |
| **No live retrieval at inference** | The chatbot does not automatically query a vector store; RAG examples are simulated at training time only (until v1.2). |
| **Tool calling is simulated** | Training includes `<|tool|>` patterns but tools are not executed during inference yet. |
| **Seed corpus size** | ~167 curated files anchor domain knowledge; synthetic expansion increases volume, not guaranteed factual novelty. |
| **No RLHF / DPO** | Alignment relies on SFT only; no preference optimization or human feedback loop. |
| **GPU required for practical training** | CPU training is possible for smoke tests but not feasible at corpus scale. |
| **Benchmark goals are targets** | Reported goals above are aspirational; results depend on hardware, hyperparameters, and training duration. |

## HuggingFace fine-tuning (alternative path)

Uses `data/advanced/train.jsonl` after running `make prepare-advanced`. Update `config/training.yaml`:

```yaml
data:
  train_file: data/advanced/train.jsonl
  val_file: data/advanced/val.jsonl
```

## Hardware recommendations

| Path | GPU | Notes |
|------|-----|-------|
| From-scratch (default config) | 16 GB+ | ~85M params, feasible on single GPU |
| From-scratch (large) | 40 GB+ | Increase `n_layers` / `d_model` in chatbot.yaml |
| HF QLoRA 1.5B | 16 GB | Default training.yaml |
| HF QLoRA 7B | 24 GB+ | Change model name |

## Customization

- **More categories**: Edit `scripts/corpus_templates.py` and `config/corpus_generation.yaml`
- **Your own chatbot persona**: Change `system_prompt` in `config/chatbot.yaml`
- **Add curated knowledge**: Drop markdown into `knowledge-base/` and re-run `make pipeline`
- **Reduce synthetic ratio**: Lower `SCALE` in `config/corpus_generation.yaml` to weight training toward seed content
