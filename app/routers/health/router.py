"""
@Author:
    Bart Kim 

@Note:

"""
import graphene
from starlette.graphql import GraphQLApp

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import esume_session_local, esume_engine, esume_base

'''
    Rest API
'''
router = APIRouter(
    prefix="/health",
    tags=["기타"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def health_check():
    return {"status": "live"}


@router.get("/request")
async def request_check(request: Request):

    resposne = {
        'host': request.client.host,
        'headers': request.headers
    }

    return resposne


'''
    GraphQL API 
'''
