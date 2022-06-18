from fastapi import APIRouter, Depends

from src.application.dependencies.db_session import db_session
from src.domain.users import user_service
from src.domain.users.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[User])
async def get_users(session=Depends(db_session)):
    return await user_service.get_users(session)


# @router.get("/{user_id}", response_model=User)
# async def get_user(user_id: UUID):
#     return await user_service.get_user(user_id)


# @router.post("/", response_model=User)
# async def create_user(user: UserCreate):
#     return await user_service.create_user(user)
