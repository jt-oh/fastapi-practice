from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from .user import MyUser

from ..database import Base

class MyItem(Base):
    __tablename__ = "my_items"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(1000))
    owner_id = Column(Integer, ForeignKey("my_users.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    owner = relationship("MyUser", back_populates="items")