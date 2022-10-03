from datetime import datetime
from typing import List
from pydantic import BaseModel

from schemas.item import MyItem

class MyUserBase(BaseModel):
    age: int

class MyUserCreate(MyUserBase):
    email: str
    password: str

class MyUserUpdate(MyUserBase):
    pass

class MyUser(MyUserBase):
    id: int
    email: str
    is_active: bool = True
    created_at: datetime
    updated_at: datetime
    items: List[MyItem] = []

    class Config:
        orm_mode = True