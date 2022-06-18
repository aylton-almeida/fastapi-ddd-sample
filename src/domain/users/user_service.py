from http import HTTPStatus
from uuid import UUID

from fastapi import HTTPException

from src.domain.users.models.user import User
from src.domain.users.models.user_create import UserCreate
from src.infrastructure.localdb import users


def get_users() -> User:
    return [User(**user) for user in users.users]


def get_user(user_id: UUID):

    if user := next((user for user in users.users if user["user_id"] == user_id), None):
        return User(**user)

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")


def create_user(user_create: UserCreate):
    user = user_create.to_user()

    users.users.append(user.dict())
    return user
