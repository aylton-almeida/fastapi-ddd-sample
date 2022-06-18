from src.infrastructure.postgresql import create_async_session


async def db_session():
    session = create_async_session()
    try:
        yield session
    finally:
        await session.close()
