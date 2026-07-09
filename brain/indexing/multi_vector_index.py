"""Multi-vector retrieval — separate embeddings for title, body, and code."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from brain.embeddings.encoder import EmbeddingEncoder
from brain.ingestion.loader import KnowledgeBase
from brain.types import Document, ScoredDocument

_CODE_FENCE = re.compile(r"```[\s\S]*?```", re.MULTILINE)


def _extract_code(content: str) -> str:
    blocks = _CODE_FENCE.findall(content)
    return "\n".join(blocks)[:4000] if blocks else ""


class MultiVectorIndex:
    """
    Indexes up to three vectors per document:
      - title (short semantic signal)
      - body (main content)
      - code (fenced code blocks when present)

    Query hits are fused with role weights for multi-vector retrieval.
    """

    ROLE_WEIGHTS = {"title": 0.35, "body": 1.0, "code": 0.85}

    def __init__(
        self,
        kb: KnowledgeBase,
        encoder: EmbeddingEncoder,
        persist_dir: str = "data/brain/multi_vector_store",
        collection_name: str = "coltex_multivec",
    ):
        self.kb = kb
        self.encoder = encoder
        self.persist_dir = Path(persist_dir)
        self.collection_name = collection_name
        self._client = None
        self._collection = None

    def _connect(self) -> None:
        if self._collection is not None:
            return
        import chromadb

        self.persist_dir.mkdir(parents=True, exist_ok=True)
        self._client = chromadb.PersistentClient(path=str(self.persist_dir))
        self._collection = self._client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"},
        )

    @property
    def is_indexed(self) -> bool:
        self._connect()
        return self._collection.count() > 0

    def _role_id(self, doc_id: str, role: str) -> str:
        return f"{doc_id}::{role}"

    def _texts_for(self, doc: Document) -> list[tuple[str, str]]:
        roles: list[tuple[str, str]] = [
            ("title", f"{doc.title}\n{doc.doc_type}\n{doc.category}"),
            ("body", doc.content[:6000]),
        ]
        code = _extract_code(doc.content)
        if code:
            roles.append(("code", code))
        return roles

    def index(self, batch_size: int = 200, max_docs: int | None = None) -> int:
        self._connect()
        total = 0
        batch_ids, batch_texts, batch_metas = [], [], []
        docs = self.kb.documents[:max_docs] if max_docs else self.kb.documents

        def flush() -> None:
            nonlocal total
            if not batch_ids:
                return
            embeddings = self.encoder.encode(batch_texts)
            self._collection.add(
                ids=batch_ids,
                documents=batch_texts,
                embeddings=embeddings,
                metadatas=batch_metas,
            )
            total += len(batch_ids)
            batch_ids.clear()
            batch_texts.clear()
            batch_metas.clear()

        for doc in docs:
            for role, text in self._texts_for(doc):
                batch_ids.append(self._role_id(doc.doc_id, role))
                batch_texts.append(text)
                batch_metas.append({
                    "doc_id": doc.doc_id,
                    "role": role,
                    "path": doc.path,
                    "title": doc.title,
                    "doc_type": doc.doc_type,
                    "category": doc.category,
                })
                if len(batch_ids) >= batch_size:
                    flush()
        flush()
        return total

    def upsert_document(self, doc: Document) -> None:
        self._connect()
        # delete existing roles then re-add
        existing_ids = [self._role_id(doc.doc_id, r) for r in ("title", "body", "code")]
        try:
            self._collection.delete(ids=existing_ids)
        except Exception:
            pass
        roles = self._texts_for(doc)
        texts = [t for _, t in roles]
        embeddings = self.encoder.encode(texts)
        self._collection.add(
            ids=[self._role_id(doc.doc_id, r) for r, _ in roles],
            documents=texts,
            embeddings=embeddings,
            metadatas=[{
                "doc_id": doc.doc_id,
                "role": role,
                "path": doc.path,
                "title": doc.title,
                "doc_type": doc.doc_type,
                "category": doc.category,
            } for role, _ in roles],
        )

    def delete_document(self, doc_id: str) -> None:
        self._connect()
        try:
            self._collection.delete(ids=[self._role_id(doc_id, r) for r in ("title", "body", "code")])
        except Exception:
            pass

    def search(self, query: str, top_k: int = 12) -> list[ScoredDocument]:
        self._connect()
        if self._collection.count() == 0:
            return []
        q_emb = self.encoder.encode_query(query)
        n = min(top_k * 3, self._collection.count())
        results = self._collection.query(query_embeddings=[q_emb], n_results=n)
        by_doc: dict[str, float] = {}
        paths = {d.doc_id: d for d in self.kb.documents}
        distances = results.get("distances", [[]])[0]
        for i, meta in enumerate(results["metadatas"][0]):
            doc_id = meta.get("doc_id", "")
            role = meta.get("role", "body")
            dist = distances[i] if i < len(distances) else 1.0
            sim = max(0.0, 1.0 - dist) * self.ROLE_WEIGHTS.get(role, 0.5)
            by_doc[doc_id] = by_doc.get(doc_id, 0.0) + sim
        ranked = sorted(by_doc.items(), key=lambda x: x[1], reverse=True)[:top_k]
        out: list[ScoredDocument] = []
        for doc_id, score in ranked:
            doc = paths.get(doc_id) or self.kb.get(doc_id)
            if doc:
                out.append(ScoredDocument(document=doc, score=score, source="multi_vector"))
        return out
