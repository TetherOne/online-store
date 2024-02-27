from core.models.order_product_association import order_product_association_table

from typing_extensions import TYPE_CHECKING

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped

from core.models.base import Base

from datetime import datetime

from sqlalchemy import func


if TYPE_CHECKING:
    from .product import Product


class Order(Base):

    promocode: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now,
    )
    products: Mapped[list['Product']] = relationship(
        secondary=order_product_association_table,
        back_populates='orders',
    )