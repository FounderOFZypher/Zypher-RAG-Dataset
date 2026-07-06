"""Fine-tune a language model on the Zypher knowledge base using LoRA SFT."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import torch
import yaml
from datasets import load_dataset
from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from trl import SFTTrainer


def load_config(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def resolve_target_modules(model, spec: str | list[str]) -> list[str]:
    if isinstance(spec, list):
        return spec

    import torch.nn as nn

    try:
        from bitsandbytes.nn import Linear4bit

        linear_types = (nn.Linear, Linear4bit)
    except ImportError:
        linear_types = (nn.Linear,)

    if spec == "all-linear":
        exclude = re.compile(r"router|route|lm_head", re.IGNORECASE)
        names: set[str] = set()
        for module_name, module in model.named_modules():
            if exclude.search(module_name):
                continue
            if isinstance(module, linear_types):
                names.add(module_name.split(".")[-1])
        resolved = sorted(names)
        if resolved:
            print(f"LoRA target_modules ({len(resolved)}): {resolved[:12]}{'...' if len(resolved) > 12 else ''}")
            return resolved

    raise ValueError(
        f"Could not resolve LoRA target_modules from spec={spec!r}. "
        "Set lora.target_modules to an explicit list in config."
    )


def formatting_func_builder(tokenizer):
    def formatting_func(example):
        messages = example["messages"]
        if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template:
            return tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=False,
            )
        parts = []
        for msg in messages:
            parts.append(f"{msg['role']}: {msg['content']}")
        return "\n".join(parts)

    return formatting_func


def main() -> None:
    parser = argparse.ArgumentParser(description="Fine-tune a causal LM with LoRA")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config/training.yaml"),
        help="Training configuration YAML file",
    )
    parser.add_argument("--train-file", type=Path, default=None)
    parser.add_argument("--val-file", type=Path, default=None)
    args = parser.parse_args()

    cfg = load_config(args.config)
    model_name = cfg["model"]["name"]
    train_file = args.train_file or Path(cfg["data"]["train_file"])
    val_file = args.val_file or Path(cfg["data"]["val_file"])
    output_dir = Path(cfg["training"]["output_dir"])

    if not train_file.exists():
        raise FileNotFoundError(
            f"Training file not found: {train_file}. Run `make prepare-advanced` first."
        )

    use_4bit = cfg["model"].get("load_in_4bit", True)
    bf16 = cfg["training"].get("bf16", torch.cuda.is_available())
    trust_remote_code = cfg["model"].get("trust_remote_code", True)

    if not torch.cuda.is_available():
        raise RuntimeError(
            "CUDA GPU required for fine-tuning. Use Google Colab with A100/L4/T4 (24GB+ for Laguna)."
        )

    tokenizer = AutoTokenizer.from_pretrained(
        model_name,
        trust_remote_code=trust_remote_code,
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    quant_config = None
    if use_4bit:
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16 if bf16 else torch.float16,
            bnb_4bit_use_double_quant=True,
        )

    model_kwargs: dict = {
        "trust_remote_code": trust_remote_code,
        "device_map": "auto",
        "torch_dtype": torch.bfloat16 if bf16 else torch.float16,
    }
    if quant_config is not None:
        model_kwargs["quantization_config"] = quant_config

    attn_impl = cfg["model"].get("attn_implementation")
    if attn_impl:
        model_kwargs["attn_implementation"] = attn_impl

    print(f"Loading model: {model_name}")
    model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)

    if use_4bit:
        model = prepare_model_for_kbit_training(
            model,
            use_gradient_checkpointing=cfg["training"].get("gradient_checkpointing", True),
        )

    if cfg["training"].get("gradient_checkpointing", True):
        model.gradient_checkpointing_enable()

    lora_cfg = cfg["lora"]
    target_modules = resolve_target_modules(model, lora_cfg.get("target_modules", "all-linear"))

    peft_config = LoraConfig(
        r=int(lora_cfg["r"]),
        lora_alpha=int(lora_cfg["alpha"]),
        lora_dropout=float(lora_cfg.get("dropout", 0.05)),
        bias="none",
        task_type=TaskType.CAUSAL_LM,
        target_modules=target_modules,
        modules_to_save=lora_cfg.get("modules_to_save"),
    )
    model = get_peft_model(model, peft_config)
    model.print_trainable_parameters()

    data_files = {"train": str(train_file)}
    if val_file.exists():
        data_files["validation"] = str(val_file)

    dataset = load_dataset("json", data_files=data_files)
    train_dataset = dataset["train"]
    eval_dataset = dataset["validation"] if "validation" in dataset else None

    train_args = TrainingArguments(
        output_dir=str(output_dir),
        num_train_epochs=cfg["training"]["num_train_epochs"],
        per_device_train_batch_size=cfg["training"]["per_device_train_batch_size"],
        per_device_eval_batch_size=cfg["training"].get("per_device_eval_batch_size", 1),
        gradient_accumulation_steps=cfg["training"]["gradient_accumulation_steps"],
        learning_rate=float(cfg["training"]["learning_rate"]),
        warmup_ratio=cfg["training"].get("warmup_ratio", 0.03),
        logging_steps=cfg["training"].get("logging_steps", 10),
        save_steps=cfg["training"].get("save_steps", 100),
        eval_strategy="steps" if eval_dataset is not None else "no",
        eval_steps=cfg["training"].get("eval_steps", 100),
        save_total_limit=cfg["training"].get("save_total_limit", 2),
        bf16=bf16,
        fp16=not bf16,
        gradient_checkpointing=cfg["training"].get("gradient_checkpointing", True),
        report_to=cfg["training"].get("report_to", "none"),
        optim=cfg["training"].get("optim", "paged_adamw_8bit" if use_4bit else "adamw_torch"),
        max_grad_norm=cfg["training"].get("max_grad_norm", 1.0),
        seed=int(cfg["training"].get("seed", 42)),
        remove_unused_columns=False,
    )

    trainer = SFTTrainer(
        model=model,
        args=train_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        processing_class=tokenizer,
        formatting_func=formatting_func_builder(tokenizer),
        max_seq_length=int(cfg["training"].get("max_seq_length", 2048)),
        packing=cfg["training"].get("packing", False),
    )

    trainer.train()
    trainer.save_model(str(output_dir / "final"))
    tokenizer.save_pretrained(str(output_dir / "final"))

    print(f"Training complete. Adapter saved to {output_dir / 'final'}")
    print(f"Inference: python3 scripts/infer.py --base-model {model_name} --adapter {output_dir / 'final'} --question 'Explain GraphRAG'")


if __name__ == "__main__":
    main()
