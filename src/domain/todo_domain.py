from dataclasses import dataclass
from sqlalchemy import Boolean, Column, Integer, String

from src.infrastructure.sqlite3_handler import Base


@dataclass
class Todo(Base):
    __tablename__ = 'todos'
    id: int = Column(Integer, primary_key=True)
    todo_name: str = Column(String(128))
    content: str = Column(String(256))
    user: str = Column(String(256))
    is_done: bool = Column(Boolean, default=False)
    