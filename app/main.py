from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import engine, SessionLocal
import crud, schemas

myApp = FastAPI()

# models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@myApp.post("/users/", response_model=schemas.MyUser, tags=["users"])
def create_user(user: schemas.MyUserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@myApp.get("/users/", response_model=List[schemas.MyUser], tags=["users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@myApp.get("/users/{user_id}", response_model=schemas.MyUser, tags=["users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@myApp.put("/users/{user_id}", response_model=schemas.MyUser, tags=["users"])
def update_user(user_id: int, user: schemas.MyUserUpdate, db: Session = Depends(get_db)):
    exist_user = crud.get_user(db, user_id=user_id)
    if exist_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return crud.update_user(db, exist_user, user)


@myApp.delete("/users/{user_id}", tags=["users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return crud.delete_user(db, db_user)


@myApp.post("/users/{user_id}/items/", response_model=schemas.MyItem, tags=["items"])
def create_item_for_user(
    user_id: int, item: schemas.MyItemUpdateOrCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@myApp.get("/items/", response_model=List[schemas.MyItem], tags=["items"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items