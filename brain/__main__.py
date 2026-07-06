"""Zypher Brain — Mega RAG Database CLI."""

from __future__ import annotations

import argparse
import json
import sys

from brain.brain import ZypherBrain


def cmd_index(args: argparse.Namespace) -> None:
    brain = ZypherBrain(config_path=args.config)
    count = brain.index(force=args.reindex)
    print(json.dumps({"indexed": count, **brain.stats()}, indent=2))


def cmd_retrieve(args: argparse.Namespace) -> None:
    brain = ZypherBrain(config_path=args.config)
    brain.index(force=False)
    result = brain.retrieve(args.query)
    print(f"Query: {args.query}\n")
    for i, scored in enumerate(result.documents, 1):
        doc = scored.document
        print(f"  [{i}] {doc.title} (score={scored.score:.2f}, source={scored.source})")
    if args.context:
        print("\n--- Context ---\n")
        print(result.context[: args.max_chars])


def cmd_stats(args: argparse.Namespace) -> None:
    brain = ZypherBrain(config_path=args.config)
    print(json.dumps(brain.stats(), indent=2))


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Zypher Brain — Mega RAG Database")
    parser.add_argument("--config", default="config/brain.yaml")
    sub = parser.add_subparsers(dest="command", required=True)

    p_index = sub.add_parser("index", help="Build vector index from knowledge base")
    p_index.add_argument("--reindex", action="store_true")
    p_index.set_defaults(func=cmd_index)

    p_retrieve = sub.add_parser("retrieve", help="Retrieve from the RAG database")
    p_retrieve.add_argument("query")
    p_retrieve.add_argument("--context", action="store_true")
    p_retrieve.add_argument("--max-chars", type=int, default=4000)
    p_retrieve.set_defaults(func=cmd_retrieve)

    p_stats = sub.add_parser("stats", help="Database statistics")
    p_stats.set_defaults(func=cmd_stats)

    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
