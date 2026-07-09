"""Shared types for Coltex."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Document:
    doc_id: str
    title: str
    path: str
    content: str
    category: str = ""
    doc_type: str = ""
    hub: str = ""
    tags: list[str] = field(default_factory=list)
    related: list[str] = field(default_factory=list)
    relationships: dict[str, list[str]] = field(default_factory=dict)


@dataclass
class ScoredDocument:
    document: Document
    score: float
    source: str  # vector | bm25 | metadata | graph | multi_vector | sql | code | api | plugin | ...


@dataclass
class RetrievalResult:
    query: str
    documents: list[ScoredDocument]
    context: str
    trace: dict | None = None
    built_context: object | None = None

    @property
    def has_context(self) -> bool:
        return bool(self.documents) and "No relevant documents" not in self.context
