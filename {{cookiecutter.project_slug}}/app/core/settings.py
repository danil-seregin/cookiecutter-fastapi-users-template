import os
from pydantic import BaseModel

class Settings(BaseModel):
    jwt_secret: str = "{{ cookiecutter.jwt_secret }}"
    user_secret: str = "{{ cookiecutter.user_secret }}"

    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", '{{ cookiecutter.access_token_expire_minutes }}'))
    permanent_token: bool = os.getenv("PERMANENT_TOKEN", "{{ cookiecutter.permanent_token }}").lower() == "on"

    database_user_url: str = os.getenv("DATABASE_USER_URL", "{{ cookiecutter.database_user_url }}")

    admin_email: str = os.getenv("ADMIN_EMAIL", "{{ cookiecutter.admin_email }}")
    admin_password: str = os.getenv("ADMIN_PASSWORD", "{{ cookiecutter.admin_password }}")

settings = Settings()
