from __future__ import annotations

from pathlib import Path

import torch

from chatbot.config import load_config
from chatbot.model import ChatbotModel
from chatbot.tokenizer import ChatbotTokenizer


class InferenceEngine:
    def __init__(self, checkpoint_dir: Path, config_path: Path = Path("config/chatbot.yaml")):
        self.config = load_config(config_path)
        checkpoint_dir = Path(checkpoint_dir)

        tok_dir = checkpoint_dir / "tokenizer"
        if not (tok_dir / "tokenizer.json").exists():
            fallback = Path("outputs/tokenizer")
            if (fallback / "tokenizer.json").exists():
                print(f"Tokenizer not in checkpoint; using {fallback}")
                tok_dir = fallback
            else:
                raise FileNotFoundError(
                    f"No tokenizer at {tok_dir} or outputs/tokenizer. Run train-tokenizer first."
                )

        self.tokenizer = ChatbotTokenizer.load(tok_dir)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = ChatbotModel.from_checkpoint(checkpoint_dir)
        self.model.to(self.device)
        self.model.eval()

        inf = self.config.inference
        self.max_new_tokens = int(inf.get("max_new_tokens", 512))
        self.temperature = float(inf.get("temperature", 0.7))
        self.top_p = float(inf.get("top_p", 0.9))

    def chat(self, messages: list[dict[str, str]]) -> str:
        if not messages or messages[0]["role"] != "system":
            messages = [{"role": "system", "content": self.config.system_prompt}] + messages

        prompt = self.tokenizer.format_chat(messages)
        input_ids = torch.tensor([self.tokenizer.encode(prompt, add_bos=True)], device=self.device)
        output = self.model.generate(
            input_ids,
            max_new_tokens=self.max_new_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
            eos_token_id=self.tokenizer.eos_token_id,
        )
        new_tokens = output[0, input_ids.size(1) :].tolist()
        return self.tokenizer.decode(new_tokens).strip()
