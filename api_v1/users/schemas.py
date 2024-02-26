from fastapi_users import schemas
from pydantic import ConfigDict, EmailStr
from pydantic import BaseModel
from typing import Optional



class UserBase(BaseModel):

    username: str
    email: EmailStr
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]


class User(UserBase):

    model_config = ConfigDict(from_attributes=True)

    id: int


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


class UserUpdate(UserBase):
    pass


class UserUpdatePartial(UserBase):

    username: str | None = None
    email: EmailStr | None = None
    is_active: Optional[bool] | None = None
    is_superuser: Optional[bool] | None = None
    is_verified: Optional[bool] | None = None

