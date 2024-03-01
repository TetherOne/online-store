from fastapi import status, Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.orders import crud
from api_v1.orders.schemas import Order

from core.models.db_helper import db_helper


router = APIRouter(tags=["Orders"])


@router.get(
    "/",
    response_model=list[Order],
    status_code=status.HTTP_200_OK,
)
async def get_orders(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):

    return await crud.get_orders(session=session)