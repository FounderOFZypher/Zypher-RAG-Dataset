#!/usr/bin/env python3
"""Export graph relationship edges from curated knowledge base."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import export_graph_edges, load_knowledge_base, load_product_config, resolve_path, write_jsonl


def main() -> None:
    parser = argparse.ArgumentParser(description="Export graph edges")
    parser.add_argument("--config", type=Path, default=Path("config/product.yaml"))
    args = parser.parse_args()

    cfg = load_product_config(args.config)
    kb = load_knowledge_base(cfg)
    out_path = resolve_path(cfg["output"]["graph"])
    edges = export_graph_edges(kb)

    write_jsonl(out_path, edges)
    print(json.dumps({
        "edges": len(edges),
        "documents": len(kb.documents),
        "output": str(out_path),
    }, indent=2))


if __name__ == "__main__":
    main()
