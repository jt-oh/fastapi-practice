from sqlalchemy.orm import Session

from ..models import MyItem
from ..schemas.item import MyItemUpdateOrCreate


class CRUDItem():

    def get_items(db: Session, skip: int = 0, limit: int = 100):
        return db.query(MyItem).offset(skip).limit(limit).all()


    def create_user_item(db: Session, item: MyItemUpdateOrCreate, user_id: int):
        db_item = MyItem(**item.dict(), owner_id=user_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        
        return db_item

item = CRUDItem()