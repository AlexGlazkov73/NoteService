from abc import ABC, abstractmethod

from sqlalchemy import select, insert, delete

from database import AsyncScopedSession


class AbstractRepository(ABC):
    @abstractmethod
    async def get_object_by_id(self, object_id: int):
        raise NotImplementedError

    @abstractmethod
    async def create_object(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete_object_by_id(self, object_id: int):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def get_object_by_id(self, object_id: int):
        """Get row from table of DB by id"""
        async with AsyncScopedSession() as session:
            query = select(self.model).where(self.model.id == object_id)
            result = await session.execute(query)
            return result.scalar()

    async def create_object(self, data: dict):
        """Insert row to table of DB"""
        async with AsyncScopedSession() as session:
            query = insert(self.model).values(**data).returning(self.model.id)
            new_object_id = await session.execute(query)
            await session.commit()
            return new_object_id.scalar_one()

    async def delete_object_by_id(self, object_id: int):
        """Delete row from table of DB by id"""
        async with AsyncScopedSession() as session:
            query = delete(self.model).where(self.model.id == object_id)
            await session.execute(query)
            await session.commit()
