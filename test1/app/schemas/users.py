from fastapi_users import schemas
from typing import Optional
import uuid

class UserRead(schemas.BaseUser[uuid.UUID]):
    role: str

class UserCreate(schemas.BaseUserCreate):
    role: Optional[str] = "worker"

class UserUpdate(schemas.BaseUserUpdate):
    role: Optional[str]