from aiocache import Cache, cached
from aiocache.serializers import PickleSerializer
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper

from .schemas import UserUpdatePartial
from .schemas import UserUpdate
from .schemas import User

from .dependencies import user_by_id

from fastapi import APIRouter
from fastapi import Depends

from starlette import status

from . import crud


router = APIRouter(tags=["Users"])

cache = Cache(Cache.REDIS, endpoint="127.0.0.1", port=6379, namespace='store')



@router.get(
    "/",
    response_model=list[User],
)
@cached(ttl=60, cache=Cache.REDIS, key="users", serializer=PickleSerializer(), namespace="store")
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_users(session=session)


@router.get(
    "/{user_id}",
    response_model=User,
)
@cached(ttl=60, cache=Cache.REDIS, key="users", serializer=PickleSerializer(), namespace="store")
async def get_user(
    user: User = Depends(user_by_id),
):

    return user


@router.put("/{user_id}")
async def update_user(
    user_update: UserUpdate,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    await cache.delete("users")

    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
    )


@router.patch("/{user_id}")
async def update_user_partial(
    user_update: UserUpdatePartial,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    await cache.delete("users")

    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
        partial=True,
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:

    await cache.delete("users")

    await crud.delete_user(
        session=session,
        user=user,
    )