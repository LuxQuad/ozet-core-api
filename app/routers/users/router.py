"""
@Author:
    Bart Kim

@Note:

"""
from tokenize import String
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from starlette.graphql import GraphQLApp

from typing import List

from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import esume_session_local, esume_engine, esume_base
from app.dependencies import get_db

'''
    Rest API
'''
router = APIRouter(
    prefix="/users",
    tags=["사용자"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, username=user.username)

    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    return crud.create_user(db=db, user=user)


@router.get("/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(crud.user.get_current_active_user)):
    return current_user


@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.user.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=crud.user.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.user.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/items/")
async def read_own_items(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(crud.user.get_current_active_user)
):
    return crud.item.get_itmes_by_user(db=db, owner_id=current_user.id)


@router.post("/items/", response_model=schemas.Item)
def create_item_for_user(
    item: schemas.ItemCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(crud.user.get_current_active_user),
):
    return crud.create_user_item(db=db, item=item, user_id=current_user.id)
