from datetime import datetime

from pydantic import BaseModel


class OrderBase(BaseModel):

    promocode: str


class Order(OrderBase):

    id: int
    created_at: datetime


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderCreate):
    pass


class OrderUpdatePartial(OrderCreate):
    pass