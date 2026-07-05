.PHONY: install generate prepare prepare-advanced pipeline train train-scratch chat clean

install:
	pip install -r requirements.txt

# Generate ~112k knowledge files at scale=1000 (use SCALE=10 for quick smoke test)
generate:
	python3 scripts/generate_corpus.py --scale $(or $(SCALE),1000)

generate-smoke:
	python3 scripts/generate_corpus.py --scale 1000 --max-files 2000

prepare:
	python3 scripts/prepare_dataset.py

prepare-advanced:
	python3 scripts/prepare_advanced_dataset.py

# Full pipeline: corpus → advanced dataset
pipeline: generate prepare-advanced
	@echo "Pipeline complete. See data/advanced/dataset_stats.json"

# HuggingFace LoRA fine-tune (uses pretrained base model)
train:
	python3 scripts/train.py --config config/training.yaml

# From-scratch chatbot pipeline
train-tokenizer:
	python3 -m chatbot.cli train-tokenizer --corpus-glob "knowledge-base/**/*.md"

train-scratch: train-tokenizer
	python3 -m chatbot.cli pretrain --data data/advanced/pretrain.txt --max-steps 2000
	python3 -m chatbot.cli sft --data data/advanced/train.jsonl --checkpoint outputs/pretrain/checkpoint-final --max-steps 3000

chat:
	python3 -m chatbot.cli chat --checkpoint outputs/sft/checkpoint-final

infer:
	python3 scripts/infer.py \
		--base-model Qwen/Qwen2.5-1.5B-Instruct \
		--adapter outputs/zyphersft/final \
		--question "How does Zypher use GraphRAG for architectural reasoning?"

clean:
	rm -rf data/ outputs/ knowledge-base/generated __pycache__ scripts/__pycache__ chatbot/__pycache__
