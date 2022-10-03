from datetime import datetime
from typing import List
from pydantic import BaseModel

class MyItemBase(BaseModel):
    title: str
    description: str = ""

class MyItemUpdateOrCreate(MyItemBase):
    pass

class MyItem(MyItemBase):
    id: int
    created_at: datetime
    updated_at: datetime
    owner_id: int

    class Config():
        orm_mode = True

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