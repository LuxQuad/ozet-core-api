from dotenv import load_dotenv

from fastapi import Depends, FastAPI, HTTPException

from app.database import esume_session_local, esume_engine, esume_base
from app.routers import items, users

load_dotenv(verbose=True)

esume_base.metadata.create_all(bind=esume_engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Hello Esume!"}
