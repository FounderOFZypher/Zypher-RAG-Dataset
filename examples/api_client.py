#!/usr/bin/env python3
"""Example: Zypher Platform REST API client."""

from __future__ import annotations

import json
import sys
import urllib.request


BASE_URL = "http://localhost:8080"


def api(method: str, path: str, body: dict | None = None) -> dict:
    url = f"{BASE_URL}{path}"
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method)
    if data:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())


def main() -> None:
    query = sys.argv[1] if len(sys.argv) > 1 else "What is RAG for code?"

    health = api("GET", "/health")
    print("Health:", json.dumps(health, indent=2))

    stats = api("GET", "/v1/stats")
    print("\nStats:", json.dumps(stats, indent=2))

    result = api("POST", "/v1/retrieve", {"query": query, "top_k": 5})
    print(f"\nRetrieve '{query}':")
    for hit in result.get("documents", [])[:5]:
        print(f"  - {hit.get('title', 'untitled')} (score={hit.get('score', 0):.2f})")


if __name__ == "__main__":
    main()
