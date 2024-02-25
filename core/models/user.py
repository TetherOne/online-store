from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped

from core.models.base import Base

from typing import TYPE_CHECKING

from sqlalchemy import String


if TYPE_CHECKING:
    from .profile import Profile


class User(Base):

    username: Mapped[str] = mapped_column(String(30))
    profile: Mapped['Profile'] = relationship(back_populates='user', cascade='all,delete')