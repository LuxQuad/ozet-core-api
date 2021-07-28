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

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import esume_session_local, esume_engine, esume_base
from app.dependencies import get_token_header, get_db

'''
    Rest API
'''
router = APIRouter(
    prefix="/users",
    tags=["사용자"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


'''
    GraphQL API
'''


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

    user = SQLAlchemyConnectionField(models.user.UserConnection)
    user_list = SQLAlchemyConnectionField(models.user.UserConnection)

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        users_query = models.user.UserGraph.get_query(info)

        if id is not None:
            return users_query.filter_by(id=id)

    def resolve_user_list(self, info, **kwargs):
        return models.user.UserGraph.get_query(info).all()


def add_graphql_route(service):
    service.add_route("/user", GraphQLApp(schema=graphene.Schema(query=Query)))
