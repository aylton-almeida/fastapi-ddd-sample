from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.users.models.user import User
from src.infrastructure.postgresql.entities.user_entity import UserEntity


async def get_users(session: AsyncSession) -> User:
    users = await UserEntity.get_all(session)

    return [User(**user.to_dict()) for user in users]


# async def get_user(user_id: UUID):

#     if user := next((user for user in users.users if user["user_id"] == user_id), None):
#         return User(**user)

#     raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")


# async def create_user(user_create: UserCreate):
#     user = user_create.to_user()

#     users.users.append(user.dict())
#     return user
