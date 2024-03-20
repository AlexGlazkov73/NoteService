from uuid import uuid4
from pydantic import BaseModel, UUID4, Field


class NoteSchema(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    text: str


class NoteSchemaAdd(BaseModel):
    text: str
