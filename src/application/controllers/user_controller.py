from fastapi import APIRouter

from src.domain.users import user_service

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/')
async def get_users():
    return user_service.get_users()


@router.get('/{user_id}')
async def get_user(user_id: int):
    return user_service.get_user(user_id)
