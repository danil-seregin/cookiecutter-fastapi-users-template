from fastapi import APIRouter, Depends
from schemas.users import UserRead, UserCreate, UserUpdate
from core.auth import auth_backend, fastapi_users, current_active_user
from dependencies.roles import is_admin

router = APIRouter()

# Авторизация
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Авторизация"],
)

# Регистрация — только админ (эндпоинт появится только для админа)
admin_router = APIRouter()
admin_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Авторизация"],
    dependencies=[Depends(is_admin)]
)

# Управление пользователями — только авторизованным
users_router = APIRouter()
users_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["Пользователи"],
    dependencies=[Depends(current_active_user)]
)
