from fastapi import status, Depends, APIRouter
from fastapi_cache.decorator import cache

from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.orders import crud
from api_v1.orders.dependencies import order_by_id
from api_v1.orders.schemas import Order

from core.models.db_helper import db_helper


router = APIRouter(tags=["Orders"])


@router.get(
    "/",
    response_model=list[Order],
    status_code=status.HTTP_200_OK,
)
@cache(60)
async def get_orders(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_orders(session=session)


@router.get(
    "/{order_id}",
    response_model=Order,
    status_code=status.HTTP_200_OK,
)
@cache(60)
async def get_order(
    order: Order = Depends(order_by_id),
):

    return order


@router.get(
    "/",
    response_model=list[Order],
    status_code=status.HTTP_200_OK,
)
async def get_orders(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_orders(session=session)