"""Incremental indexing — upsert / delete without full rebuild."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol

from brain.types import Document


class SupportsUpsert(Protocol):
    def upsert_document(self, doc: Document) -> None: ...
    def delete_document(self, doc_id: str) -> None: ...


@dataclass
class IncrementalIndexReport:
    upserted: list[str] = field(default_factory=list)
    deleted: list[str] = field(default_factory=list)
    refreshed: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {
            "upserted": self.upserted,
            "deleted": self.deleted,
            "refreshed": self.refreshed,
            "errors": self.errors,
            "ok": not self.errors,
        }


class IncrementalIndexer:
    """
    Coordinates incremental updates across vector, multi-vector, BM25,
    metadata, and specialized indexes.
    """

    def __init__(
        self,
        vector_index=None,
        multi_vector_index=None,
        bm25_index=None,
        metadata_index=None,
        specialized: list | None = None,
    ):
        self.vector_index = vector_index
        self.multi_vector_index = multi_vector_index
        self.bm25_index = bm25_index
        self.metadata_index = metadata_index
        self.specialized = specialized or []

    def upsert(self, doc: Document) -> IncrementalIndexReport:
        report = IncrementalIndexReport()
        try:
            if self.vector_index is not None:
                # prefer upsert if available, else add
                if hasattr(self.vector_index, "upsert_document"):
                    self.vector_index.upsert_document(doc)
                else:
                    self.vector_index.index_document(doc)
                report.upserted.append("vector")
        except Exception as exc:
            report.errors.append(f"vector: {exc}")

        try:
            if self.multi_vector_index is not None:
                self.multi_vector_index.upsert_document(doc)
                report.upserted.append("multi_vector")
        except Exception as exc:
            report.errors.append(f"multi_vector: {exc}")

        try:
            if self.bm25_index is not None:
                self.bm25_index.refresh()
                report.refreshed.append("bm25")
        except Exception as exc:
            report.errors.append(f"bm25: {exc}")

        try:
            if self.metadata_index is not None:
                self.metadata_index.refresh()
                report.refreshed.append("metadata")
        except Exception as exc:
            report.errors.append(f"metadata: {exc}")

        for spec in self.specialized:
            try:
                name = getattr(spec, "source", spec.__class__.__name__)
                spec.refresh()
                report.refreshed.append(name)
            except Exception as exc:
                report.errors.append(f"{getattr(spec, 'source', 'specialized')}: {exc}")

        return report

    def delete(self, doc_id: str) -> IncrementalIndexReport:
        report = IncrementalIndexReport()
        try:
            if self.vector_index is not None and hasattr(self.vector_index, "delete_document"):
                self.vector_index.delete_document(doc_id)
                report.deleted.append("vector")
        except Exception as exc:
            report.errors.append(f"vector: {exc}")

        try:
            if self.multi_vector_index is not None:
                self.multi_vector_index.delete_document(doc_id)
                report.deleted.append("multi_vector")
        except Exception as exc:
            report.errors.append(f"multi_vector: {exc}")

        try:
            if self.bm25_index is not None:
                self.bm25_index.delete(doc_id)
                report.deleted.append("bm25")
        except Exception as exc:
            report.errors.append(f"bm25: {exc}")

        try:
            if self.metadata_index is not None:
                self.metadata_index.refresh()
                report.refreshed.append("metadata")
        except Exception as exc:
            report.errors.append(f"metadata: {exc}")

        for spec in self.specialized:
            try:
                spec.refresh()
                report.refreshed.append(getattr(spec, "source", "specialized"))
            except Exception as exc:
                report.errors.append(f"{getattr(spec, 'source', 'specialized')}: {exc}")

        return report
