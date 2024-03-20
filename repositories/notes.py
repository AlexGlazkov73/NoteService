from .base import SQLAlchemyRepository
from database import Note


class NoteRepository(SQLAlchemyRepository):
    model = Note
