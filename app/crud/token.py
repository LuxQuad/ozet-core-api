"""
@Author:
    Bart Kim 

@Note:

"""
from sqlalchemy.orm import Session

from app import models, schemas


def check_token(db: Session, skip: int = 0, limit: int = 100):
    return None


def create_token(db: Session, user: schemas.UserCreate):
    return None
