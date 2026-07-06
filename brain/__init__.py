"""Zypher Brain — Mega RAG Database engine."""

from brain.brain import ZypherBrain
from brain.types import Document, RetrievalResult, ScoredDocument

__version__ = "3.0.0"
__all__ = [
    "ZypherBrain",
    "Document",
    "RetrievalResult",
    "ScoredDocument",
]
