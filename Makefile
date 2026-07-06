.PHONY: install validate generate prepare prepare-advanced pipeline train train-scratch chat clean

install:
	pip install -r requirements.txt

validate:
	python3 scripts/validate_pipeline.py

validate-pretrain:
	python3 scripts/validate_pipeline.py --require-checkpoint pretrain

validate-sft:
	python3 scripts/validate_pipeline.py --require-checkpoint sft

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

# HuggingFace LoRA fine-tune (default: Qwen 1.5B)
train:
	python3 scripts/train.py --config config/training.yaml

# Laguna XS 2.1 QLoRA fine-tune (poolside/Laguna-XS-2.1)
train-laguna:
	python3 scripts/train.py --config config/training_laguna.yaml

pipeline-laguna: generate-smoke prepare-advanced train-laguna

# From-scratch chatbot pipeline
train-tokenizer:
	python3 -m chatbot.cli train-tokenizer --corpus-glob "knowledge-base/**/*.md"

train-scratch:
	$(MAKE) train-tokenizer
	python3 scripts/validate_pipeline.py --require-tokenizer
	python3 -m chatbot.cli pretrain --data data/advanced/pretrain.txt --batch-size 1 --max-steps 2000
	python3 scripts/validate_pipeline.py --require-checkpoint pretrain
	python3 -m chatbot.cli sft --data data/advanced/train.jsonl --checkpoint outputs/pretrain/checkpoint-final --batch-size 1 --max-steps 3000
	python3 scripts/validate_pipeline.py --require-checkpoint sft

chat:
	python3 -m chatbot.cli chat --checkpoint outputs/sft/checkpoint-final

infer:
	python3 scripts/infer.py \
		--base-model Qwen/Qwen2.5-1.5B-Instruct \
		--adapter outputs/zyphersft/final \
		--question "How does Zypher use GraphRAG for architectural reasoning?"

infer-laguna:
	python3 scripts/infer.py \
		--base-model poolside/Laguna-XS-2.1 \
		--adapter outputs/laguna-xs-2.1-sft/final \
		--question "Explain GraphRAG for code architecture."

clean:
	rm -rf data/ outputs/ knowledge-base/generated __pycache__ scripts/__pycache__ chatbot/__pycache__
