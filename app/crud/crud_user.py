from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from .. import models
from ..schemas.user import *


class CRUDUser():

    def get_user(self, db: Session, user_id: int) -> models.MyUser:
        return db.get(models.MyUser, user_id)


    def get_user_by_email(self, db: Session, email: str):
        return db.query(models.MyUser).filter(models.MyUser.email == email).first()


    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.MyUser).offset(skip).limit(limit).all()


    def create_user(self, db: Session, user: MyUserCreate):
        fake_hashed_password = user.password + "notreallyhashed"

        now = datetime.now()

        db_user = models.MyUser(email=user.email, age=user.age, hashed_password=fake_hashed_password, created_at=now, updated_at=now)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    def update_user(self, db: Session, exist_user: models.MyUser, user: MyUserUpdate):
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
        

    def delete_user(self, db: Session, user: models.MyUser):
        user_id = user.id

        db.delete(user)
        db.commit()

        return user_id

user = CRUDUser()