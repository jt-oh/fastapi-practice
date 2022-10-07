from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from ..models import MyUser
from ..schemas.user import MyUserCreate, MyUserUpdate


class CRUDUser():

    def get_user(self, db: Session, user_id: int) -> MyUser:
        return db.get(MyUser, user_id)


    def get_user_by_email(self, db: Session, email: str):
        return db.query(MyUser).filter(MyUser.email == email).first()


    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(MyUser).offset(skip).limit(limit).all()


    def create_user(self, db: Session, user: MyUserCreate):
        fake_hashed_password = user.password + "notreallyhashed"

        now = datetime.now()

        db_user = MyUser(email=user.email, age=user.age, hashed_password=fake_hashed_password, created_at=now, updated_at=now)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user


    def update_user(self, db: Session, exist_user: MyUser, user: MyUserUpdate):
        exist_user_obj = jsonable_encoder(exist_user)
        update_data = user.dict(exclude_unset=True)

        for field in exist_user_obj:
            if field in update_data:
                setattr(exist_user, field, update_data[field])
        setattr(exist_user, "updated_at", datetime.now())

        # below Session.add() can be omitted as Session does flush
        # dirty models before Session.commit().
        # And model has been dirty since attribute changes.
        db.add(exist_user)
        db.commit()
        db.refresh(exist_user)

        return exist_user
        

    def delete_user(self, db: Session, user: MyUser):
        user_id = user.id

        db.delete(user)
        db.commit()

        return user_id

user = CRUDUser()