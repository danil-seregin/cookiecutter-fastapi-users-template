import os
from pydantic import BaseModel

class Settings(BaseModel):
    jwt_secret: str = "9f11e6425539fd14f51b50a91e47437e"
    user_secret: str = "25d3a358d9929073000cca1e4d0db635"

    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", '60'))
    permanent_token: bool = os.getenv("PERMANENT_TOKEN", "on").lower() == "on"

    database_user_url: str = os.getenv("DATABASE_USER_URL", "sqlite+aiosqlite:///./users.db")

    admin_email: str = os.getenv("ADMIN_EMAIL", "danil.ceregin@bk.ru")
    admin_password: str = os.getenv("ADMIN_PASSWORD", "Alexandr2019!@#$")

settings = Settings()
