from uuid import uuid4
from sqlalchemy import MetaData, String
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from config import DB_SCHEMA


class Base(DeclarativeBase):
    metadata = MetaData(schema=DB_SCHEMA)


class Note(Base):
    __tablename__ = 'notes'

    id = mapped_column(UUID, primary_key=True, comment='Идентификатор записки', default=uuid4)
    text = mapped_column(String, comment='Текст записки')
