from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr
from utils import camel_case_to_snake_case
from core.config import settings
from sqlalchemy import MetaData


class Base(DeclarativeBase):
    __abstract__ = True

    metadata: MetaData = MetaData(naming_convention=settings.db.naming_convention)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{camel_case_to_snake_case(cls.__name__)}s"
