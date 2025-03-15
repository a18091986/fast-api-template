from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .mixins.int_id_pk import IntIdPkMixin

class User(Base, IntIdPkMixin):
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)

    
