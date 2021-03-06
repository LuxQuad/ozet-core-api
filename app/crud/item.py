"""
@Author:
    Bart Kim 

@Note:

"""

from sqlalchemy.orm import Session

from app import models, schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_itmes_by_user(owner_id: int, db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).filter(models.Item.owner_id == owner_id).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item
