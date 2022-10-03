from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.MyUser).filter(models.MyUser.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.MyUser).filter(models.MyUser.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyUser).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.MyUserCreate):
    fake_hashed_password = user.password + "notreallyhashed"

    now = datetime.now()

    db_user = models.MyUser(email=user.email, age=user.age, hashed_password=fake_hashed_password, created_at=now, updated_at=now)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def update_user(db: Session, exist_user: schemas.MyUser, user: schemas.MyUserUpdate):
    exist_user_obj = jsonable_encoder(exist_user)
    update_data = user.dict(exclude_unset=True)

    for field in exist_user_obj:
        if field in update_data:
            setattr(exist_user, field, update_data[field])

    setattr(exist_user, "updated_at", datetime.now())
    db.add(exist_user)
    db.commit()
    db.refresh(exist_user)

    return exist_user
    

def delete_user(db: Session, user: schemas.MyUser):
    user_id = user.id

    db.delete(user)
    db.commit()

    return user_id

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MyItem).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.MyItemUpdateOrCreate, user_id: int):
    db_item = models.MyItem(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    return db_item