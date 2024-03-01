from datetime import datetime

from pydantic import BaseModel


class OrderBase(BaseModel):

    promocode: str
    created_at: datetime


class Order(OrderBase):

    id: int


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderCreate):
    pass


class OrderUpdatePartial(OrderCreate):
    pass