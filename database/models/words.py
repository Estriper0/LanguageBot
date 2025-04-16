from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class Words(Base):
    __tablename__ = 'words'
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(index=True)
    word_eng: Mapped[str] = mapped_column(unique=True)
    word_rus: Mapped[str]
    
