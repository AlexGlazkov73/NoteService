from uuid import UUID
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas import NoteSchemaAdd
from services import NoteService, Encryption
from repositories import NoteRepository

notes = APIRouter(tags=['notes'])


def init_note_service():
    return NoteService(NoteRepository, Encryption)


@notes.post('/generate')
async def create_note(
        note: NoteSchemaAdd,
        note_service: NoteService = Depends(init_note_service),
):
    note_id = await note_service.add_note(note)
    response = {'note_id': jsonable_encoder(note_id)}
    return JSONResponse(content=response, status_code=201)


@notes.get('/secrets/{note_id}')
async def get_note(
        note_id: UUID,
        note_service: NoteService = Depends(init_note_service),
):
    note = await note_service.get_note(note_id)
    if not note:
        return JSONResponse(
            content={"message": "Note not found"},
            status_code=404,
        )
    await note_service.delete_note(note_id)
    return note
