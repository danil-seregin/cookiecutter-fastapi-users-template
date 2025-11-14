from uuid import uuid4
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.settings import settings
from app.db.users import users_engine
from app.models.users import User


async def ensure_admin_created():
    """
    Создает администратора при старте приложения,
    если его нет в базе.
    """
    async with AsyncSession(users_engine) as session:
        result = await session.execute(
            select(User).where(User.email == settings.admin_email)
        )
        existing_user = result.scalars().first()

        if existing_user:
            return

        pwd_context = PasswordHash.recommended()
        hashed = pwd_context.hash(settings.admin_password)

        admin_user = User(
            id=uuid4(),
            email=settings.admin_email,
            hashed_password=hashed,
            is_active=True,
            is_superuser=True,
            is_verified=True,
            role="admin",
        )

        session.add(admin_user)
        await session.commit()
        print(f"Администратор {settings.admin_email} создан")
