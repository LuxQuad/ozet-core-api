"""
@Author:
    Bart Kim 

@Note:

"""
import graphene
from starlette.graphql import GraphQLApp

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import esume_session_local, esume_engine, esume_base
from app.dependencies import get_token_header, get_db

'''
    Rest API
'''
router = APIRouter(
    prefix="/health",
    tags=["기타"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    return {"status": "live"}


'''
    GraphQL API 
'''
