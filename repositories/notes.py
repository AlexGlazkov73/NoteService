from .base import SQLAlchemyRepository
from database import Note


class NoteRepository(SQLAlchemyRepository):
    """Repository for working with the Note model"""
    model = Note
