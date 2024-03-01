from typing import Annotated

from fastapi import Path, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status

from api_v1.orders import crud
from core.models import Order
from core.models.db_helper import db_helper


async def order_by_id(
    order_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Order:

    order = await crud.get_order(
        session=session,
        order_id=order_id,
    )

    if order is not None:
        return order

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Order {order_id} not found!",
    )
