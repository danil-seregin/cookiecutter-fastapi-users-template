import uuid
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import BearerTransport, JWTStrategy, AuthenticationBackend
from app.managers.users import get_user_manager
from app.models.users import User
from app.core.settings import settings

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    if settings.permanent_token:
        lifetime = 10 * 365 * 24 * 60 * 60
    else:
        lifetime = settings.access_token_expire_minutes * 60

    return JWTStrategy(
        secret=settings.jwt_secret,
        lifetime_seconds=lifetime,
    )

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

current_active_user = fastapi_users.current_user(active=True)
