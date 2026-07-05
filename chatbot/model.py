from __future__ import annotations

import math

import torch
import torch.nn as nn
import torch.nn.functional as F


def precompute_rope_freqs(dim: int, seq_len: int, theta: float = 10000.0) -> torch.Tensor:
    freqs = 1.0 / (theta ** (torch.arange(0, dim, 2).float() / dim))
    positions = torch.arange(seq_len)
    angles = torch.outer(positions, freqs)
    return torch.cat([angles, angles], dim=-1)


def apply_rope(x: torch.Tensor, freqs: torch.Tensor) -> torch.Tensor:
    # x: (batch, heads, seq, head_dim)
    seq_len = x.size(2)
    freqs = freqs[:seq_len].to(x.device)
    cos = freqs.cos()[None, None, :, :]
    sin = freqs.sin()[None, None, :, :]
    x1, x2 = x[..., ::2], x[..., 1::2]
    rotated = torch.stack([x1 * cos[..., ::2] - x2 * sin[..., ::2], x1 * sin[..., ::2] + x2 * cos[..., ::2]], dim=-1)
    return rotated.flatten(-2)


class RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        norm = x.pow(2).mean(dim=-1, keepdim=True)
        return x * torch.rsqrt(norm + self.eps) * self.weight


class SwiGLU(nn.Module):
    def __init__(self, d_model: int, d_ff: int, dropout: float):
        super().__init__()
        self.w1 = nn.Linear(d_model, d_ff, bias=False)
        self.w2 = nn.Linear(d_model, d_ff, bias=False)
        self.w3 = nn.Linear(d_ff, d_model, bias=False)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.dropout(self.w3(F.silu(self.w1(x)) * self.w2(x)))


class CausalSelfAttention(nn.Module):
    def __init__(self, d_model: int, n_heads: int, dropout: float, max_seq_len: int, rope_theta: float):
        super().__init__()
        if d_model % n_heads != 0:
            raise ValueError("d_model must be divisible by n_heads")
        self.n_heads = n_heads
        self.head_dim = d_model // n_heads
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=False)
        self.out = nn.Linear(d_model, d_model, bias=False)
        self.dropout = nn.Dropout(dropout)
        self.register_buffer("freqs", precompute_rope_freqs(self.head_dim, max_seq_len, rope_theta), persistent=False)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        batch, seq_len, _ = x.shape
        qkv = self.qkv(x).reshape(batch, seq_len, 3, self.n_heads, self.head_dim)
        q, k, v = qkv.unbind(dim=2)
        q = q.transpose(1, 2)
        k = k.transpose(1, 2)
        v = v.transpose(1, 2)

        q = apply_rope(q, self.freqs)
        k = apply_rope(k, self.freqs)

        scores = (q @ k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        causal = torch.triu(torch.ones(seq_len, seq_len, device=x.device), diagonal=1).bool()
        scores = scores.masked_fill(causal, float("-inf"))
        if mask is not None:
            scores = scores.masked_fill(mask[:, None, None, :] == 0, float("-inf"))

        attn = self.dropout(scores.softmax(dim=-1))
        out = attn @ v
        out = out.transpose(1, 2).reshape(batch, seq_len, -1)
        return self.out(out)


class TransformerBlock(nn.Module):
    def __init__(self, d_model: int, n_heads: int, d_ff: int, dropout: float, max_seq_len: int, rope_theta: float):
        super().__init__()
        self.norm1 = RMSNorm(d_model)
        self.attn = CausalSelfAttention(d_model, n_heads, dropout, max_seq_len, rope_theta)
        self.norm2 = RMSNorm(d_model)
        self.mlp = SwiGLU(d_model, d_ff, dropout)

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        x = x + self.attn(self.norm1(x), mask)
        x = x + self.mlp(self.norm2(x))
        return x


class ChatbotModel(nn.Module):
    """Decoder-only transformer for from-scratch chatbot training."""

    def __init__(
        self,
        vocab_size: int,
        max_seq_len: int = 2048,
        d_model: int = 768,
        n_heads: int = 12,
        n_layers: int = 12,
        d_ff: int = 3072,
        dropout: float = 0.1,
        rope_theta: float = 10000.0,
    ):
        super().__init__()
        self.max_seq_len = max_seq_len
        self.token_emb = nn.Embedding(vocab_size, d_model)
        self.drop = nn.Dropout(dropout)
        self.layers = nn.ModuleList(
            [
                TransformerBlock(d_model, n_heads, d_ff, dropout, max_seq_len, rope_theta)
                for _ in range(n_layers)
            ]
        )
        self.norm = RMSNorm(d_model)
        self.lm_head = nn.Linear(d_model, vocab_size, bias=False)
        self.lm_head.weight = self.token_emb.weight
        self.apply(self._init_weights)

    def _init_weights(self, module: nn.Module) -> None:
        if isinstance(module, nn.Linear):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)
        elif isinstance(module, nn.Embedding):
            nn.init.normal_(module.weight, mean=0.0, std=0.02)

    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor | None = None) -> torch.Tensor:
        if input_ids.size(1) > self.max_seq_len:
            raise ValueError(f"Sequence length {input_ids.size(1)} exceeds max_seq_len {self.max_seq_len}")

        x = self.drop(self.token_emb(input_ids))
        for layer in self.layers:
            x = layer(x, attention_mask)
        x = self.norm(x)
        return self.lm_head(x)

    @torch.no_grad()
    def generate(
        self,
        input_ids: torch.Tensor,
        max_new_tokens: int = 256,
        temperature: float = 0.8,
        top_p: float = 0.9,
        eos_token_id: int | None = None,
    ) -> torch.Tensor:
        self.eval()
        generated = input_ids
        for _ in range(max_new_tokens):
            context = generated[:, -self.max_seq_len :]
            logits = self.forward(context)[:, -1, :]
            logits = logits / max(temperature, 1e-5)
            probs = torch.softmax(logits, dim=-1)
            sorted_probs, sorted_idx = torch.sort(probs, descending=True)
            cumulative = torch.cumsum(sorted_probs, dim=-1)
            mask = cumulative > top_p
            mask[..., 0] = False
            sorted_probs = sorted_probs.masked_fill(mask, 0.0)
            sorted_probs = sorted_probs / sorted_probs.sum(dim=-1, keepdim=True)
            next_token = sorted_idx.gather(-1, torch.multinomial(sorted_probs, 1))
            generated = torch.cat([generated, next_token], dim=-1)
            if eos_token_id is not None and (next_token == eos_token_id).all():
                break
        return generated

    def count_parameters(self) -> int:
        return sum(p.numel() for p in self.parameters())

    def save_pretrained(self, directory: str) -> None:
        from pathlib import Path

        path = Path(directory)
        path.mkdir(parents=True, exist_ok=True)
        torch.save(self.state_dict(), path / "model.pt")
        config = {
            "vocab_size": self.lm_head.out_features,
            "max_seq_len": self.max_seq_len,
        }
        (path / "config.json").write_text(__import__("json").dumps(config, indent=2), encoding="utf-8")

    @classmethod
    def load_pretrained(cls, directory: str, **model_kwargs) -> "ChatbotModel":
        from pathlib import Path

        path = Path(directory) / "model.pt"
        model = cls(**model_kwargs)
        model.load_state_dict(torch.load(path, map_location="cpu"))
        return model
