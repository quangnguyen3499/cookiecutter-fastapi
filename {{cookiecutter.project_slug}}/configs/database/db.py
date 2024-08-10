from typing import Any

from pydantic import BaseModel
from pydantic.alias_generators import to_camel
from sqlalchemy import create_engine
from sqlalchemy import CursorResult
from sqlalchemy import Insert
from sqlalchemy import MetaData
from sqlalchemy import Select
from sqlalchemy import Update
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from configs.common_config import settings
from core.constants import DB_NAMING_CONVENTION


DATABASE_URI = str(settings.DATABASE_URI)

metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base(
    metadata=metadata,
)


class HealthcheckModel(BaseModel):
    status: str = "ok"


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        populate_by_name = True


async def fetch_one(select_query: Select | Insert | Update) -> dict[str, Any] | None:
    async with engine.begin() as conn:
        cursor: CursorResult = await conn.execute(select_query)
        return cursor.first()._asdict() if cursor.rowcount() > 0 else None


async def fetch_all(select_query: Select | Insert | Update) -> list[dict[str, Any]]:
    async with engine.begin() as conn:
        cursor: CursorResult = await conn.execute(select_query)
        return [r._asdict() for r in cursor.all()]


async def execute(select_query: Insert | Update) -> None:
    async with engine.begin() as conn:
        await conn.execute(select_query)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
