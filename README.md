# Zypher Training Data — Custom Chatbot & Advanced Fine-Tuning

Build your **own chatbot from scratch** or fine-tune a pretrained model on a **massively expanded** knowledge corpus (~1000× the original seed data).

## What's included

| Layer | Description |
|-------|-------------|
| **Corpus generator** | Produces ~112k knowledge files across 30 categories and 15 document types |
| **Advanced dataset prep** | 10+ task types: multi-turn, chain-of-thought, tool calling, RAG, code gen/review |
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
├── knowledge-base/               # Seed corpus (167 files)
│   └── generated/                # Generated corpus (~112k files at scale=1000)
├── scripts/
│   ├── generate_corpus.py        # Mass corpus generator
│   ├── prepare_advanced_dataset.py  # Advanced multi-task JSONL builder
│   ├── prepare_dataset.py        # Original simple prep (seed only)
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

# 1. Generate ~112k knowledge files (use SCALE=10 for a quick smoke test)
make generate              # SCALE=1000 default
# make generate-smoke      # SCALE=10 → ~1,125 files

# 2. Build advanced training data (target: 500k–1M+ examples)
make prepare-advanced

# 3a. Train YOUR chatbot from scratch
make train-scratch
make chat

# 3b. OR fine-tune a pretrained model with LoRA
make train
```

## Corpus scale

| `SCALE` | Generated files | Training examples (approx.) |
|---------|-----------------|----------------------------|
| 10 | ~1,125 | ~8,000 |
| 100 | ~11,250 | ~80,000 |
| 1000 | ~112,500 | ~800,000+ |

```bash
SCALE=1000 make generate
python3 scripts/prepare_advanced_dataset.py
```

## Advanced training task types

The advanced dataset builder creates multiple examples per knowledge file:

- `faq` / `documentation` — single-turn Q&A
- `multi_turn_dialogue` — follow-up conversations
- `chain_of_thought` — reasoning with `<|think|>` blocks
- `tool_calling` — simulated tool use with `<|tool|>` / `<|tool_result|>`
- `rag_with_context` — context-grounded answers
- `code_generation` / `code_review` — code tasks from walkthroughs

## From-scratch chatbot

### Architecture (default ~85M parameters)

- Decoder-only Transformer
- RoPE positional encoding
- RMSNorm + SwiGLU FFN
- BPE tokenizer with chat markers: `<|user|>`, `<|assistant|>`, `<|tool|>`, etc.

Edit `config/chatbot.yaml` to scale `d_model`, `n_layers`, and `vocab_size`.

### Training stages

```bash
# Stage 1: Train tokenizer on full corpus
python3 -m chatbot.cli train-tokenizer --corpus-glob "knowledge-base/**/*.md"

# Stage 2: Pretrain on raw text
python3 -m chatbot.cli pretrain --data data/advanced/pretrain.txt --max-steps 50000

# Stage 3: Supervised fine-tune on chat JSONL
python3 -m chatbot.cli sft \
  --data data/advanced/train.jsonl \
  --checkpoint outputs/pretrain/checkpoint-final \
  --max-steps 30000

# Stage 4: Chat
python3 -m chatbot.cli chat --checkpoint outputs/sft/checkpoint-final
```

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
- **Add knowledge**: Drop markdown into `knowledge-base/` and re-run `make pipeline`
