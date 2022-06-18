from http import HTTPStatus

from fastapi import HTTPException

from src.infrastructure.localdb import users


def get_users():
    return users.users


def get_user(user_id: int):

    if user := next((user for user in users.users if user['user_id'] == user_id), None):
        return user

    raise HTTPException(
        status_code=HTTPStatus.NOT_FOUND,
        detail='User not found'
    )
