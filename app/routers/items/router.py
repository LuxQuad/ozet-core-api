"""
@Author:
    Bart Kim 

@Note:

"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate

from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import esume_session_local, esume_engine, esume_base
from app.dependencies import get_db

router = APIRouter(
    prefix="/items",
    tags=["아이템"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

'''
    Rest API
'''


@router.get("/", response_model=Page[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return paginate(items)


'''
    GraphQL API 
'''
