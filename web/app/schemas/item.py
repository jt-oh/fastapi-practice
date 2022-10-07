from datetime import datetime
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