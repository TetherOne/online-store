from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache

from api_v1.orders.schemas import OrderUpdatePartial
from api_v1.orders.schemas import Order

from api_v1.orders.dependencies import order_by_id

from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper

from api_v1.orders import crud

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status


router = APIRouter(tags=["Orders"])


@router.get(
    "/",
    response_model=list[Order],
    status_code=status.HTTP_200_OK,
)
@cache(namespace='store', expire=60)
async def get_orders(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_orders(session=session)


@router.get(
    "/{order_id}",
    response_model=Order,
    status_code=status.HTTP_200_OK,
)
@cache(namespace='store', expire=60)
async def get_order(
    order: Order = Depends(order_by_id),
):

    return order


@router.delete(
    "/{order_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_order(
    order_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    await FastAPICache.clear(namespace='store')

    await crud.delete_order(session=session, order_id=order_id)


@router.patch("/{order_id}")
async def update_order_partial(
    order_update: OrderUpdatePartial,
    order: Order = Depends(order_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    await FastAPICache.clear(namespace='store')

    return await crud.update_order(
        session=session,
        order=order,
        order_update=order_update,
    )
