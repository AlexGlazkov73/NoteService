from asyncio import current_task

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.schema import CreateSchema
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_scoped_session,
    async_sessionmaker
)

from config import DB_URL, DB_SCHEMA
from .models import Base

engine = create_async_engine(
    DB_URL,
    pool_pre_ping=True,
    pool_size=30,
    pool_recycle=300,
)

async_session_factory = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
AsyncScopedSession = async_scoped_session(
    async_session_factory, scopefunc=current_task
)


async def init_db():
    async with engine.begin() as conn:
        await conn.execute(CreateSchema(DB_SCHEMA, if_not_exists=True))
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
