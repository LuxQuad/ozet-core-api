"""
@Author:
    Bart Kim 

@Note:

"""

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

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
