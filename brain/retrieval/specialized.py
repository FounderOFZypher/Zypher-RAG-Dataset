"""Specialized retrievers: SQL, Code, and API document retrieval."""

from __future__ import annotations

import re
from typing import Iterable

from brain.ingestion.loader import KnowledgeBase
from brain.types import Document, ScoredDocument

_TOKEN_RE = re.compile(r"[a-z0-9_./{}:-]+", re.IGNORECASE)

SQL_DOC_TYPES = frozenset({"sql_example", "database_schema", "migration_guide"})
CODE_DOC_TYPES = frozenset({"code_walkthrough", "code_review", "tutorial", "guide", "best_practices"})
API_DOC_TYPES = frozenset({"api_reference", "documentation", "design_document", "release_notes"})

SQL_HINTS = ("sql", "select", "insert", "update", "delete", "join", "index", "schema", "table", "postgres", "mysql", "query")
CODE_HINTS = ("function", "class", "method", "implement", "code", "snippet", "refactor", "bug", "stack", "traceback")
API_HINTS = ("api", "endpoint", "rest", "graphql", "openapi", "http", "request", "response", "status code", "auth header")

_HTTP_METHOD = re.compile(r"\b(GET|POST|PUT|PATCH|DELETE|HEAD|OPTIONS)\b", re.IGNORECASE)
_PATH_RE = re.compile(r"(/[a-zA-Z0-9_\-{}]+)+")
_SQL_KW = re.compile(
    r"\b(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|JOIN|WHERE|GROUP BY|ORDER BY|INDEX|TABLE)\b",
    re.IGNORECASE,
)
_CODE_IDENT = re.compile(r"\b([A-Z][a-zA-Z0-9]+|[a-z_][a-z0-9_]{2,})\b")


def _tokens(text: str) -> set[str]:
    return set(_TOKEN_RE.findall(text.lower()))


def _overlap_score(query: str, doc: Document, body_limit: int = 4000) -> float:
    q = _tokens(query)
    if not q:
        return 0.0
    blob = f"{doc.title} {' '.join(doc.tags)} {doc.content[:body_limit]}".lower()
    d = _tokens(blob)
    return len(q & d) / max(len(q), 1)


class ModeRetriever:
    """Base helper for doc-type-scoped lexical + structural retrieval."""

    source: str = "mode"
    doc_types: frozenset[str] = frozenset()
    hints: tuple[str, ...] = ()

    def __init__(self, kb: KnowledgeBase):
        self.kb = kb
        self._pool: list[Document] = []
        self.refresh()

    def refresh(self) -> None:
        self._pool = [d for d in self.kb.documents if d.doc_type in self.doc_types]
        if not self._pool:
            # fallback: hint-based soft pool from full corpus
            self._pool = [
                d for d in self.kb.documents
                if any(h in (d.title + d.content[:500]).lower() for h in self.hints[:5])
            ][:2000]

    def _base_score(self, query: str, doc: Document) -> float:
        score = _overlap_score(query, doc)
        q = query.lower()
        if doc.doc_type in self.doc_types:
            score += 0.35
        if any(h in q for h in self.hints):
            score += 0.1
        if doc.category and doc.category.lower() in q:
            score += 0.15
        return score

    def search(self, query: str, top_k: int = 10) -> list[ScoredDocument]:
        scored: list[ScoredDocument] = []
        for doc in self._pool:
            score = self.score(query, doc)
            if score > 0.12:
                scored.append(ScoredDocument(document=doc, score=score, source=self.source))
        scored.sort(key=lambda s: s.score, reverse=True)
        return scored[:top_k]

    def score(self, query: str, doc: Document) -> float:
        return self._base_score(query, doc)


class SQLRetriever(ModeRetriever):
    """Retrieve SQL examples, schemas, and migration docs with SQL-aware boosting."""

    source = "sql"
    doc_types = SQL_DOC_TYPES
    hints = SQL_HINTS

    def score(self, query: str, doc: Document) -> float:
        score = self._base_score(query, doc)
        content = doc.content
        sql_hits = len(_SQL_KW.findall(content[:5000]))
        score += min(0.4, sql_hits * 0.04)
        q_upper = query.upper()
        for kw in ("SELECT", "JOIN", "INDEX", "SCHEMA", "TABLE"):
            if kw in q_upper and kw in content.upper():
                score += 0.08
        return min(score, 1.5)


class CodeRetriever(ModeRetriever):
    """Retrieve code walkthroughs and implementation docs with identifier boosting."""

    source = "code"
    doc_types = CODE_DOC_TYPES
    hints = CODE_HINTS

    def score(self, query: str, doc: Document) -> float:
        score = self._base_score(query, doc)
        fences = len(re.findall(r"```", doc.content[:6000]))
        score += min(0.35, fences * 0.05)
        q_idents = set(_CODE_IDENT.findall(query))
        if q_idents:
            body_idents = set(_CODE_IDENT.findall(doc.content[:6000]))
            score += min(0.4, 0.08 * len(q_idents & body_idents))
        if "```" in doc.content:
            score += 0.1
        return min(score, 1.5)


class APIRetriever(ModeRetriever):
    """Retrieve API references with HTTP method / path matching."""

    source = "api"
    doc_types = API_DOC_TYPES
    hints = API_HINTS

    def score(self, query: str, doc: Document) -> float:
        score = self._base_score(query, doc)
        methods = {m.upper() for m in _HTTP_METHOD.findall(query)}
        paths = set(_PATH_RE.findall(query))
        content = doc.content[:6000]
        for m in methods:
            if re.search(rf"\b{m}\b", content):
                score += 0.15
        for p in paths:
            if p in content:
                score += 0.25
        if doc.doc_type == "api_reference":
            score += 0.2
        if "openapi" in content.lower() or "endpoint" in content.lower():
            score += 0.1
        return min(score, 1.6)
