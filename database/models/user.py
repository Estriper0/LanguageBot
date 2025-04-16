from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(index=True, unique=True)
    score: Mapped[int]

