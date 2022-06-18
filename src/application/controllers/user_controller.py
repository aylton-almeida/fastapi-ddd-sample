from uuid import UUID

from fastapi import APIRouter

from src.domain.users import user_service
from src.domain.users.models.user_create import UserCreate
from src.domain.users.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[User])
async def get_users():
    return user_service.get_users()


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: UUID):
    return user_service.get_user(user_id)


@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    return user_service.create_user(user)
