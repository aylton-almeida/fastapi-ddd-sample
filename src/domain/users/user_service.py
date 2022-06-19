from http import HTTPStatus
from typing import Awaitable
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.users.models.user import User
from src.domain.users.models.user_create import UserCreate
from src.infrastructure.postgresql.entities.user_entity import UserEntity


async def get_users(session: AsyncSession) -> Awaitable[list[User]]:
    users = await UserEntity.get_all(session)

    return [User.from_orm(user) for user in users]


async def get_user(session: AsyncSession, user_id: UUID) -> Awaitable[User]:

    user = await UserEntity.get_one(session, user_id)

    if user:
        return User.from_orm(user)

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")


async def create_user(
    session: AsyncSession, user_create: UserCreate
) -> Awaitable[User]:

    user_entity = UserEntity(**user_create.dict())
    await user_entity.save(session)

    return User.from_orm(user_entity)
