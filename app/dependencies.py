"""
@Author:
    Bart Kim 

@Note:

"""
from fastapi import Header, HTTPException
from app.settings import settings

from app.database import esume_session_local, esume_engine, esume_base


async def get_db():
    db = esume_session_local()

    try:
        yield db
    finally:
        db.close()
