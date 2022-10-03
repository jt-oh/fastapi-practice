from typing import List

from fastapi import APIRouter

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from api.deps import *
from schemas.item import *

router = APIRouter(tags=["items"])

@router.post("/users/{user_id}/items/", response_model=MyItem, tags=["items"])
def create_item_for_user(
    user_id: int, item: MyItemUpdateOrCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=List[MyItem], tags=["items"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items