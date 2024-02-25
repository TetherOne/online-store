from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Profile
from core.models.db_helper import db_helper

from .dependencies import user_by_id

from fastapi import APIRouter
from fastapi import Depends

from starlette import status

from .schemas import UserUpdatePartial
from .schemas import UserUpdate
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
async def create_user(
        user_in: UserCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    user = await crud.create_user(session=session, user_in=user_in)

    profile = Profile(user_id=user.id)
    session.add(profile)
    await session.commit()

    return user


@user_router.put("/{user_id}")
async def update_user(
    user_update: UserUpdate,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
    )


@user_router.patch("/{user_id}")
async def update_user_partial(
    user_update: UserUpdatePartial,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update,
        partial=True,
    )


@user_router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:

    await crud.delete_user(
        session=session,
        user=user,
    )