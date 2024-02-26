from fastapi_users import schemas

from pydantic import BaseModel
from pydantic import EmailStr

from typing import Optional


class User(BaseModel):

    id: int
    username: str
    email: EmailStr
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]


class UserRead(schemas.BaseUser[int]):

    id: int
    username: str
    email: EmailStr
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]


class UserCreate(schemas.BaseUserCreate):

    username: str
    password: str
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(User):

    pass


class UserUpdatePartial(User):

    username: str | None = None
    email: EmailStr | None = None
    is_active: Optional[bool] | None = None
    is_superuser: Optional[bool] | None = None
    is_verified: Optional[bool] | None = None

