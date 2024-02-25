from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper

from .dependencies import user_by_id

from fastapi import APIRouter
from fastapi import Depends

from starlette import status

from .schemas import UserCreate
from .schemas import User

from . import crud


user_router = APIRouter(tags=["Users"])


@user_router.get(
    "/",
    response_model=list[User],
)
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_users(session=session)


@user_router.get(
    "/{user_id}",
    response_model=User,
)
async def get_user(
    user: User = Depends(user_by_id),
):

    return user


@user_router.post(
    "/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    product_in: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.create_user(session=session, product_in=product_in)
