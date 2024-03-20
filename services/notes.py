from uuid import UUID
from repositories import AbstractRepository
from schemas import NoteSchemaAdd
from .encryption import AbstractEncryption


class NoteService:
    """Service for working with notes.
    :param note_repo: A repository for working with data from database
    :param encryption_service: A service for encrypting the text of the note
    """

    def __init__(self, note_repo: AbstractRepository, encryption_service: AbstractEncryption):
        self.repo = note_repo()
        self.encryption_service = encryption_service()

    async def get_note(self, note_id: UUID | str):
        """Get a note by its UUID"""
        note = await self.repo.get_object_by_id(note_id)
        if note is not None:
            note.text = self.encryption_service.decrypt(note.text)
        return note

    async def add_note(self, note_schema: NoteSchemaAdd):
        """Create note with encrypted text"""
        note_dict = note_schema.model_dump()
        note_dict['text'] = self.encryption_service.encrypt(note_dict['text'])
        new_task_id = await self.repo.create_object(note_dict)
        return new_task_id

    async def delete_note(self, note_id: UUID | str):
        """Delete a note by its UUID"""
        await self.repo.delete_object_by_id(note_id)
