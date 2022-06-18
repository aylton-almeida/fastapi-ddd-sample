from __future__ import annotations

from uuid import uuid4

from sqlalchemy import Column, Integer, String, select
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .. import Base


class UserEntity(Base):
    __tablename__ = "users"
    query: any

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    password = Column(String, nullable=False)

    @staticmethod
    async def get_all(session: AsyncSession) -> list[UserEntity]:
        result: Result = await session.execute(select(UserEntity))
        return result.scalars().all()
