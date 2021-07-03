import os

from fastapi import Header, HTTPException

from app.database import esume_session_local, esume_engine, esume_base

X_TOKEN = os.getenv('X_TOKEN')
TOKEN = os.getenv('TOKEN')

async def get_token_header(x_token: str = Header(...)):
    if x_token != X_TOKEN:
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != TOKEN:
        raise HTTPException(status_code=400, detail="No Jessica token provided")
    

async def get_db():
    db = esume_session_local()
    try:
        yield db
    finally:
        db.close()
