from __future__ import annotations

import math
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from chatbot.dataset import PretrainDataset, SFTDataset
from chatbot.model import ChatbotModel
from chatbot.tokenizer import ChatbotTokenizer


class Trainer:
    def __init__(
        self,
        model: ChatbotModel,
        tokenizer: ChatbotTokenizer,
        output_dir: Path,
        learning_rate: float = 3e-4,
        batch_size: int = 4,
        grad_accum: int = 4,
        max_steps: int = 1000,
        mixed_precision: bool = True,
    ):
        self.model = model
        self.tokenizer = tokenizer
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.batch_size = batch_size
        self.grad_accum = grad_accum
        self.max_steps = max_steps
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.optimizer = torch.optim.AdamW(model.parameters(), lr=learning_rate, weight_decay=0.01)
        self.scaler = torch.cuda.amp.GradScaler(enabled=mixed_precision and self.device.type == "cuda")
        self.criterion = nn.CrossEntropyLoss(ignore_index=-100)

    def _step(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        input_ids = batch["input_ids"].to(self.device)
        labels = batch["labels"].to(self.device)
        with torch.cuda.amp.autocast(enabled=self.scaler.is_enabled()):
            logits = self.model(input_ids)
            loss = self.criterion(logits.view(-1, logits.size(-1)), labels.view(-1))
        return loss

    def train_loop(self, dataset: PretrainDataset | SFTDataset) -> None:
        if len(dataset) == 0:
            raise ValueError(
                "Training dataset is empty. Run `make prepare-advanced` and check data files exist."
            )

        drop_last = len(dataset) >= self.batch_size
        loader = DataLoader(
            dataset,
            batch_size=self.batch_size,
            shuffle=True,
            drop_last=drop_last,
        )
        self.model.train()
        step = 0
        running_loss = 0.0
        steps_since_log = 0

        while step < self.max_steps:
            epoch_batches = 0
            for batch in loader:
                epoch_batches += 1
                loss = self._step(batch) / self.grad_accum
                self.scaler.scale(loss).backward()
                running_loss += loss.item()
                steps_since_log += 1

                if (step + 1) % self.grad_accum == 0:
                    self.scaler.step(self.optimizer)
                    self.scaler.update()
                    self.optimizer.zero_grad(set_to_none=True)

                if step % 50 == 0:
                    avg = running_loss / max(1, steps_since_log)
                    print(f"step={step} loss={avg:.4f} perplexity={math.exp(min(avg, 20)):.2f}")

                if step > 0 and step % 500 == 0:
                    self.save_checkpoint(step)

                step += 1
                if step >= self.max_steps:
                    break

            if epoch_batches == 0:
                raise ValueError(
                    f"No training batches produced (dataset={len(dataset)}, batch_size={self.batch_size}). "
                    "Lower --batch-size or add more training data."
                )

        self.save_checkpoint("final")

    def save_checkpoint(self, tag: str | int) -> None:
        ckpt_dir = self.output_dir / f"checkpoint-{tag}"
        ckpt_dir.mkdir(parents=True, exist_ok=True)
        self.model.save_pretrained(str(ckpt_dir))
        self.tokenizer.save(ckpt_dir / "tokenizer")
        print(f"Saved checkpoint to {ckpt_dir}")
