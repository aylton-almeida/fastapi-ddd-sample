from uuid import UUID

from fastapi import APIRouter, Depends

from src.domain.users import user_service
from src.domain.users.models.user import User
from src.domain.users.models.user_create import UserCreate
from src.infrastructure.postgresql import db_utils

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[User])
async def get_users(session=Depends(db_utils.get_db_session)):
    return await user_service.get_users(session)


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: UUID, session=Depends(db_utils.get_db_session)):
    return await user_service.get_user(session, user_id)


@router.post("/", response_model=User)
async def create_user(user: UserCreate, session=Depends(db_utils.get_db_session)):
    return await user_service.create_user(session, user)
