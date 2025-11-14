from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker
from app.core.settings import settings

DATABASE_URL = settings.database_user_url

users_engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    echo=False,
)

UserStringAsyncSessionLocal = async_sessionmaker(
    bind=users_engine,
    expire_on_commit=False,
    autoflush=False,
)

async def get_users_async_db():
    async with UserStringAsyncSessionLocal() as session:
        yield session
