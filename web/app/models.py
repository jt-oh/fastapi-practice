from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

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

class MyItem(Base):
    __tablename__ = "my_items"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(1000))
    owner_id = Column(Integer, ForeignKey("my_users.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    owner = relationship("MyUser", back_populates="items")