from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import torch
from torch.utils.data import Dataset


class PretrainDataset(Dataset):
    """Next-token prediction on raw text lines."""

    def __init__(self, path: Path, tokenizer, max_seq_len: int):
        self.tokenizer = tokenizer
        self.max_seq_len = max_seq_len
        self.samples: list[list[int]] = []
        if not path.exists():
            raise FileNotFoundError(f"Pretrain data not found: {path}")
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                ids = tokenizer.encode(line, add_bos=True) + [tokenizer.eos_token_id]
                for start in range(0, max(1, len(ids) - 1), max_seq_len):
                    chunk = ids[start : start + max_seq_len + 1]
                    if len(chunk) >= 2:
                        self.samples.append(chunk)

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> dict[str, torch.Tensor]:
        ids = self.samples[idx]
        pad_id = self.tokenizer.pad_token_id
        if len(ids) < self.max_seq_len + 1:
            ids = ids + [pad_id] * (self.max_seq_len + 1 - len(ids))
        else:
            ids = ids[: self.max_seq_len + 1]
        x = torch.tensor(ids[:-1], dtype=torch.long)
        y = torch.tensor(ids[1:], dtype=torch.long)
        y[y == pad_id] = -100
        return {"input_ids": x, "labels": y}


class SFTDataset(Dataset):
    """Supervised fine-tuning on chat JSONL."""

    def __init__(self, path: Path, tokenizer, max_seq_len: int):
        self.tokenizer = tokenizer
        self.max_seq_len = max_seq_len
        self.samples: list[list[int]] = []

        with path.open(encoding="utf-8") as handle:
            for line in handle:
                row: dict[str, Any] = json.loads(line)
                messages = row["messages"]
                text = tokenizer.format_chat(messages)
                ids = tokenizer.encode(text, add_bos=True) + [tokenizer.eos_token_id]
                if len(ids) > max_seq_len + 1:
                    ids = ids[: max_seq_len + 1]
                if len(ids) >= 2:
                    self.samples.append(ids)

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> dict[str, torch.Tensor]:
        ids = self.samples[idx]
        pad_id = self.tokenizer.pad_token_id
        if len(ids) < self.max_seq_len + 1:
            ids = ids + [pad_id] * (self.max_seq_len + 1 - len(ids))
        x = torch.tensor(ids[:-1], dtype=torch.long)
        y = torch.tensor(ids[1:], dtype=torch.long)
        y[y == pad_id] = -100
        return {"input_ids": x, "labels": y}
