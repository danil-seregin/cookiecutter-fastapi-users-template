from fastapi import Depends, HTTPException, status
from app.models.users import User
from app.core.auth import fastapi_users

current_active_user = fastapi_users.current_user(active=True)

def role_required(*roles: str):
    async def checker(user: User = Depends(current_active_user)):
        if user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Недостаточно прав"
            )
        return user
    return checker

is_admin = role_required("admin")
is_head = role_required("head")
is_worker = role_required("worker")
