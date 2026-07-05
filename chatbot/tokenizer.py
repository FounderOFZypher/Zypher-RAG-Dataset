from __future__ import annotations

import json
import re
from pathlib import Path

from tokenizers import Tokenizer, models, normalizers, pre_tokenizers, trainers


DEFAULT_SPECIAL_TOKENS = [
    "<|pad|>",
    "<|bos|>",
    "<|eos|>",
    "<|user|>",
    "<|assistant|>",
    "<|system|>",
    "<|tool|>",
    "<|tool_result|>",
    "<|think|>",
    "<|/think|>",
]


class ChatbotTokenizer:
    """BPE tokenizer with chat special tokens."""

    def __init__(self, tokenizer: Tokenizer, special_tokens: list[str] | None = None):
        self._tok = tokenizer
        self.special_tokens = special_tokens or DEFAULT_SPECIAL_TOKENS
        self.token_to_id = {tok: self._tok.token_to_id(tok) for tok in self.special_tokens}
        self.id_to_token = {idx: tok for tok, idx in self.token_to_id.items()}

    @property
    def vocab_size(self) -> int:
        return self._tok.get_vocab_size()

    @property
    def pad_token_id(self) -> int:
        return self.token_to_id["<|pad|>"]

    @property
    def bos_token_id(self) -> int:
        return self.token_to_id["<|bos|>"]

    @property
    def eos_token_id(self) -> int:
        return self.token_to_id["<|eos|>"]

    def encode(self, text: str, add_bos: bool = False) -> list[int]:
        ids = self._tok.encode(text).ids
        if add_bos:
            return [self.bos_token_id] + ids
        return ids

    def decode(self, ids: list[int], skip_special: bool = True) -> str:
        text = self._tok.decode(ids, skip_special_tokens=skip_special)
        return text

    def format_chat(self, messages: list[dict[str, str]]) -> str:
        parts: list[str] = []
        role_map = {
            "system": "<|system|>",
            "user": "<|user|>",
            "assistant": "<|assistant|>",
            "tool": "<|tool|>",
        }
        for message in messages:
            marker = role_map.get(message["role"], "<|user|>")
            parts.append(f"{marker}\n{message['content']}\n")
        parts.append("<|assistant|>\n")
        return "".join(parts)

    def save(self, directory: Path) -> None:
        directory.mkdir(parents=True, exist_ok=True)
        self._tok.save(str(directory / "tokenizer.json"))
        meta = {"special_tokens": self.special_tokens, "vocab_size": self.vocab_size}
        (directory / "tokenizer_config.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, directory: Path) -> "ChatbotTokenizer":
        tok = Tokenizer.from_file(str(directory / "tokenizer.json"))
        config_path = directory / "tokenizer_config.json"
        special = DEFAULT_SPECIAL_TOKENS
        if config_path.exists():
            special = json.loads(config_path.read_text(encoding="utf-8")).get("special_tokens", special)
        return cls(tok, special)

    @classmethod
    def train_from_corpus(
        cls,
        corpus_paths: list[Path],
        output_dir: Path,
        vocab_size: int = 32000,
        special_tokens: list[str] | None = None,
    ) -> "ChatbotTokenizer":
        special_tokens = special_tokens or DEFAULT_SPECIAL_TOKENS
        tokenizer = Tokenizer(models.BPE(unk_token="<|pad|>"))
        tokenizer.normalizer = normalizers.NFC()
        tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)

        trainer = trainers.BpeTrainer(
            vocab_size=vocab_size,
            special_tokens=special_tokens,
            min_frequency=2,
            show_progress=True,
        )

        files = [str(path) for path in corpus_paths if path.exists()]
        if not files:
            raise FileNotFoundError("No corpus files found for tokenizer training")

        tokenizer.train(files, trainer)
        chat_tok = cls(tokenizer, special_tokens)
        chat_tok.save(output_dir)
        return chat_tok

    @classmethod
    def train_from_glob(cls, pattern: str, output_dir: Path, vocab_size: int = 32000) -> "ChatbotTokenizer":
        paths = sorted(Path(".").glob(pattern))
        text_file = output_dir / "_corpus_merged.txt"
        output_dir.mkdir(parents=True, exist_ok=True)
        with text_file.open("w", encoding="utf-8") as out:
            for path in paths:
                try:
                    out.write(path.read_text(encoding="utf-8"))
                    out.write("\n")
                except OSError:
                    continue
        return cls.train_from_corpus([text_file], output_dir, vocab_size=vocab_size)
