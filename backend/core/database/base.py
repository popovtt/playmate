from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_session
)
from sqlalchemy.orm import sessionmaker

from backend.core.config import DATABASE_URL

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")


engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db():
    async with async_session() as session:
        yield session