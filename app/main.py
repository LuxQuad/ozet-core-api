from app.routers.items import router
import os
from dotenv import load_dotenv

from fastapi import Depends, FastAPI, HTTPException

from app.database import esume_session_local, esume_engine, esume_base
from app import routers


'''
    Load Environments
'''
load_dotenv(verbose=True)

'''
    DB Migrate
'''
esume_base.metadata.create_all(bind=esume_engine)


'''
    Fast API Module Initial
'''
tags_metadata = [
    {
        "name": "사용자",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "아이템",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    title=os.getenv('SERVICE_NAME'),
    description=os.getenv('SERVICE_DESC'),
    verison=os.getenv('SERVICE_VERSION'),
    openapi_tags=tags_metadata
)


'''
    Fast API Router Initial
'''
app.include_router(routers.users.router)
app.include_router(routers.items.router)
app.include_router(routers.health.router)
