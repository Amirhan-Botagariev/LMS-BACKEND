from typing import Optional

from fastapi_users import schemas
from fastapi_users.schemas import CreateUpdateDictModel
from pydantic import EmailStr


class BaseUserCreate(CreateUpdateDictModel):
    email: EmailStr
    password: str


class UserRead(schemas.BaseUser[int]):
    email: str
    role: str
    is_active: bool = True
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str


class UserUpdate(schemas.BaseUserUpdate):
    password: Optional[str]
    email: Optional[str]
    is_active: Optional[bool]
    is_verified: Optional[bool]
