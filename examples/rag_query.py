#!/usr/bin/env python3
"""Example: retrieve from the Mega RAG Database."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from brain.brain import ZypherBrain


def main() -> None:
    query = sys.argv[1] if len(sys.argv) > 1 else "What is RAG for code?"
    brain = ZypherBrain(config_path="config/brain.yaml")
    brain.index(force=False)

    result = brain.retrieve(query)
    print(f"Query: {query}\n")
    for i, scored in enumerate(result.documents, 1):
        doc = scored.document
        print(f"  [{i}] {doc.title} (score={scored.score:.2f})")

    print("\n--- Context preview ---\n")
    print(result.context[:2000])


if __name__ == "__main__":
    main()
