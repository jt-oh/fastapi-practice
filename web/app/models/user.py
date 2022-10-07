from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .item import MyItem

from ..database import Base

class MyUser(Base):
    __tablename__ = "my_users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(500))
    age = Column(Integer)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    items = relationship("MyItem", back_populates="owner")