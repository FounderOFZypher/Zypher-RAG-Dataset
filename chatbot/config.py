from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass
class ModelConfig:
    vocab_size: int = 32000
    max_seq_len: int = 2048
    d_model: int = 768
    n_heads: int = 12
    n_layers: int = 12
    d_ff: int = 3072
    dropout: float = 0.1
    rope_theta: float = 10000.0


@dataclass
class ChatbotConfig:
    model: ModelConfig
    system_prompt: str
    special_tokens: list[str]
    inference: dict[str, Any]


def load_config(path: Path | str = "config/chatbot.yaml") -> ChatbotConfig:
    with Path(path).open(encoding="utf-8") as handle:
        raw = yaml.safe_load(handle)

    model_raw = raw["model"]
    model = ModelConfig(
        vocab_size=int(model_raw["vocab_size"]),
        max_seq_len=int(model_raw["max_seq_len"]),
        d_model=int(model_raw["d_model"]),
        n_heads=int(model_raw["n_heads"]),
        n_layers=int(model_raw["n_layers"]),
        d_ff=int(model_raw["d_ff"]),
        dropout=float(model_raw.get("dropout", 0.1)),
        rope_theta=float(model_raw.get("rope_theta", 10000.0)),
    )
    return ChatbotConfig(
        model=model,
        system_prompt=raw["chatbot"]["system_prompt"].strip(),
        special_tokens=list(raw["tokenizer"]["special_tokens"]),
        inference=dict(raw.get("inference", {})),
    )
