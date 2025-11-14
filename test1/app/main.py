from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import uuid4

from app.routers import users, default, whatsapp
from app.models.users import UsersBase
from app.models.whatsapp import Base as WhatsappBase
from app.db.users import users_engine
from app.db.whatsapp import wa_engine
from app.core.create_admin import ensure_admin_created


@asynccontextmanager
async def lifespan(app_api: FastAPI):
    # Создание таблиц USERS
    async with users_engine.begin() as conn:
        await conn.run_sync(UsersBase.metadata.create_all)

    # Создание администратора
    await ensure_admin_created()

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(users.router)
app.include_router(users.admin_router)
app.include_router(users.users_router)
app.include_router(default.router)
