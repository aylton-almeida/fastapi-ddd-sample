import os
from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("DB_SERVER_URL")

__engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL.replace("://", "+asyncpg://"), future=True
)
create_async_session: Callable[[], AsyncSession] = sessionmaker(
    autocommit=False, autoflush=False, bind=__engine, class_=AsyncSession
)

Base = declarative_base()
