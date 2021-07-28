"""
@Author:
    Bart Kim 

@Note:

"""

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import esume_session_local, esume_engine, esume_base
from app.dependencies import get_token_header, get_db

router = APIRouter(
    prefix="/sentry",
    tags=["Sentry"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

'''
    Rest API
'''


@router.get("/check", response_model=Optional[int])
def check_sentry():
    division_by_zero = 1 / 0

    return division_by_zero


'''
    GraphQL API 
'''
