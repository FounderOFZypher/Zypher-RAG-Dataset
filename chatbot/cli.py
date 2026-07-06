#!/usr/bin/env python3
"""CLI entrypoints for the custom from-scratch chatbot."""

from __future__ import annotations

import argparse
from pathlib import Path

from chatbot.config import load_config
from chatbot.dataset import PretrainDataset, SFTDataset
from chatbot.inference import InferenceEngine
from chatbot.model import ChatbotModel
from chatbot.tokenizer import ChatbotTokenizer
from chatbot.trainer import Trainer


def resolve_checkpoint(path: str | Path) -> Path:
    """Return a checkpoint directory containing model.pt."""
    ckpt = Path(path)
    if (ckpt / "model.pt").exists():
        return ckpt

    search_dir = ckpt.parent if ckpt.name.startswith("checkpoint") else ckpt
    candidates = sorted(search_dir.glob("checkpoint-*"), key=lambda p: p.name)
    for candidate in reversed(candidates):
        if (candidate / "model.pt").exists():
            print(f"Using checkpoint: {candidate}")
            return candidate

    raise FileNotFoundError(
        f"No model.pt found at {ckpt} or under {search_dir}/checkpoint-*. "
        "Run pretrain first and confirm it prints 'Saved checkpoint to ... checkpoint-final'."
    )

def cmd_train_tokenizer(args: argparse.Namespace) -> None:
    cfg = load_config(args.config)
    output = Path(args.output or "outputs/tokenizer")
    ChatbotTokenizer.train_from_glob(
        args.corpus_glob,
        output,
        vocab_size=cfg.model.vocab_size,
    )
    print(f"Tokenizer saved to {output}")


def cmd_pretrain(args: argparse.Namespace) -> None:
    import yaml

    cfg = load_config(args.config)
    with Path(args.config).open(encoding="utf-8") as handle:
        raw_cfg = yaml.safe_load(handle)
    pretrain_cfg = raw_cfg.get("training", {}).get("pretrain", {})

    tokenizer = ChatbotTokenizer.load(Path(args.tokenizer))
    model = ChatbotModel(
        vocab_size=tokenizer.vocab_size,
        max_seq_len=cfg.model.max_seq_len,
        d_model=cfg.model.d_model,
        n_heads=cfg.model.n_heads,
        n_layers=cfg.model.n_layers,
        d_ff=cfg.model.d_ff,
        dropout=cfg.model.dropout,
        rope_theta=cfg.model.rope_theta,
    )
    print(f"Model parameters: {model.count_parameters():,}")

    dataset = PretrainDataset(Path(args.data), tokenizer, cfg.model.max_seq_len)
    print(f"Pretrain samples: {len(dataset):,}")
    if len(dataset) == 0:
        raise SystemExit(
            f"ERROR: No pretrain samples in {args.data}. Run `make prepare-advanced` first."
        )

    trainer = Trainer(
        model,
        tokenizer,
        Path(args.output or "outputs/pretrain"),
        learning_rate=float(pretrain_cfg.get("learning_rate", 3e-4)),
        batch_size=args.batch_size,
        max_steps=args.max_steps,
    )
    trainer.train_loop(dataset)


def cmd_sft(args: argparse.Namespace) -> None:
    cfg = load_config(args.config)
    tokenizer = ChatbotTokenizer.load(Path(args.tokenizer))

    if args.checkpoint:
        model = ChatbotModel.from_checkpoint(resolve_checkpoint(args.checkpoint))
    else:
        print("WARNING: No pretrain checkpoint — SFT starting from random weights.")
        model = ChatbotModel(
            vocab_size=tokenizer.vocab_size,
            max_seq_len=cfg.model.max_seq_len,
            d_model=cfg.model.d_model,
            n_heads=cfg.model.n_heads,
            n_layers=cfg.model.n_layers,
            d_ff=cfg.model.d_ff,
            dropout=cfg.model.dropout,
            rope_theta=cfg.model.rope_theta,
        )

    dataset = SFTDataset(Path(args.data), tokenizer, cfg.model.max_seq_len)
    print(f"SFT samples: {len(dataset):,}")

    trainer = Trainer(
        model,
        tokenizer,
        Path(args.output or "outputs/sft"),
        learning_rate=args.lr,
        batch_size=args.batch_size,
        max_steps=args.max_steps,
    )
    trainer.train_loop(dataset)


def cmd_chat(args: argparse.Namespace) -> None:
    engine = InferenceEngine(Path(args.checkpoint), Path(args.config))
    history: list[dict[str, str]] = []

    print("Custom Chatbot — type 'quit' to exit\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"quit", "exit"}:
            break
        history.append({"role": "user", "content": user_input})
        reply = engine.chat(history)
        print(f"Bot: {reply}\n")
        history.append({"role": "assistant", "content": reply})


def main() -> None:
    parser = argparse.ArgumentParser(description="Custom from-scratch chatbot")
    sub = parser.add_subparsers(dest="command", required=True)

    p_tok = sub.add_parser("train-tokenizer", help="Train BPE tokenizer on corpus")
    p_tok.add_argument("--corpus-glob", default="knowledge-base/**/*.md")
    p_tok.add_argument("--output", default="outputs/tokenizer")
    p_tok.add_argument("--config", default="config/chatbot.yaml")
    p_tok.set_defaults(func=cmd_train_tokenizer)

    p_pre = sub.add_parser("pretrain", help="Pretrain transformer from scratch")
    p_pre.add_argument("--data", default="data/advanced/pretrain.txt")
    p_pre.add_argument("--tokenizer", default="outputs/tokenizer")
    p_pre.add_argument("--output", default="outputs/pretrain")
    p_pre.add_argument("--config", default="config/chatbot.yaml")
    p_pre.add_argument("--batch-size", type=int, default=4)
    p_pre.add_argument("--max-steps", type=int, default=2000)
    p_pre.set_defaults(func=cmd_pretrain)

    p_sft = sub.add_parser("sft", help="Supervised fine-tune on chat JSONL")
    p_sft.add_argument("--data", default="data/advanced/train.jsonl")
    p_sft.add_argument("--tokenizer", default="outputs/tokenizer")
    p_sft.add_argument("--checkpoint", default=None, help="Optional pretrain checkpoint dir")
    p_sft.add_argument("--output", default="outputs/sft")
    p_sft.add_argument("--config", default="config/chatbot.yaml")
    p_sft.add_argument("--batch-size", type=int, default=2)
    p_sft.add_argument("--max-steps", type=int, default=3000)
    p_sft.add_argument("--lr", type=float, default=2e-5)
    p_sft.set_defaults(func=cmd_sft)

    p_chat = sub.add_parser("chat", help="Interactive chat with trained model")
    p_chat.add_argument("--checkpoint", default="outputs/sft/checkpoint-final")
    p_chat.add_argument("--config", default="config/chatbot.yaml")
    p_chat.set_defaults(func=cmd_chat)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
