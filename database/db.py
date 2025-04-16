from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


engine = create_async_engine('sqlite+aiosqlite:///database.db')
session_maker = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass