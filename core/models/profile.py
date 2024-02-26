from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped

from sqlalchemy import ForeignKey

from core.models.base import Base

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .user import User


class Profile(Base):

    city: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), unique=True)
    user: Mapped['User'] = relationship(back_populates='profile')