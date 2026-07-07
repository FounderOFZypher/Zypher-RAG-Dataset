"""Advanced Coltex Knowledge Corpus architecture definitions."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
ARCH_PATH = ROOT / "config" / "brain_architecture.yaml"


@dataclass(frozen=True)
class CortexLayer:
    slug: str
    path: str
    role: str
    latency_ms: int


@dataclass(frozen=True)
class BrainLobe:
    slug: str
    path: str
    role: str
    domains: tuple[str, ...]


@dataclass(frozen=True)
class MemoryTier:
    slug: str
    path: str
    role: str
    capacity_docs: int | None = None
    ttl_hours: int | None = None


@dataclass(frozen=True)
class HubRegistryEntry:
    slug: str
    lobe: str
    tier: str


def load_architecture(path: Path | None = None) -> dict[str, Any]:
    p = path or ARCH_PATH
    with p.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def cortex_layers(cfg: dict[str, Any] | None = None) -> list[CortexLayer]:
    cfg = cfg or load_architecture()
    out: list[CortexLayer] = []
    for slug, data in (cfg.get("cortex_layers") or {}).items():
        out.append(CortexLayer(
            slug=slug,
            path=data["path"],
            role=data["role"],
            latency_ms=int(data.get("latency_ms", 50)),
        ))
    return out


def brain_lobes(cfg: dict[str, Any] | None = None) -> list[BrainLobe]:
    cfg = cfg or load_architecture()
    out: list[BrainLobe] = []
    for slug, data in (cfg.get("lobes") or {}).items():
        out.append(BrainLobe(
            slug=slug,
            path=data["path"],
            role=data["role"],
            domains=tuple(data.get("domains") or []),
        ))
    return out


def memory_tiers(cfg: dict[str, Any] | None = None) -> list[MemoryTier]:
    cfg = cfg or load_architecture()
    mem = cfg.get("memory") or {}
    out: list[MemoryTier] = []
    for slug, data in mem.items():
        out.append(MemoryTier(
            slug=slug,
            path=data["path"],
            role=data["role"],
            capacity_docs=data.get("capacity_docs"),
            ttl_hours=data.get("ttl_hours"),
        ))
    return out


def hub_registry(cfg: dict[str, Any] | None = None) -> list[HubRegistryEntry]:
    cfg = cfg or load_architecture()
    out: list[HubRegistryEntry] = []
    for entry in cfg.get("hub_registry") or []:
        out.append(HubRegistryEntry(
            slug=entry["slug"],
            lobe=entry["lobe"],
            tier=entry["tier"],
        ))
    return out


def domain_to_lobe(cfg: dict[str, Any] | None = None) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for lobe in brain_lobes(cfg):
        for domain in lobe.domains:
            mapping[domain] = lobe.slug
    return mapping


def all_architecture_domains(cfg: dict[str, Any] | None = None) -> list[str]:
    cfg = cfg or load_architecture()
    domains: set[str] = set()
    for lobe in brain_lobes(cfg):
        domains.update(lobe.domains)
    for cat in (cfg.get("knowledge_corpus", {}) or {}).get("priority_domains", []):
        domains.add(cat)
    return sorted(domains)


PATHWAY_TYPES = (
    "excitatory",
    "inhibitory",
    "modulatory",
    "associative",
    "commissural",
)

ADVANCED_RELATIONSHIPS = (
    "extends",
    "validates",
    "contradicts",
    "synthesizes",
    "triggers",
    "inhibits",
    "supersedes",
    "derived_from",
    "tested_by",
    "deployed_via",
)
