from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from api.deps import *
from schemas.user import *
from schemas.item import *

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=MyUser)
def create_user(user: MyUserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=List[MyUser])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=MyUser)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}", response_model=MyUser)
def update_user(user_id: int, user: MyUserUpdate, db: Session = Depends(get_db)):
    exist_user = crud.get_user(db, user_id=user_id)
    if exist_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.update_user(db, exist_user, user)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.delete_user(db, db_user)