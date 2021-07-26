"""
@Author:
    Bart Kim 

@Note:

"""
from fastapi import Depends, FastAPI, HTTPException

from app.settings import settings
from app.database import esume_session_local, esume_engine, esume_base

from app import middleware
from app import routers


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


service = FastAPI(
    title=settings.SERVICE_NAME,
    description=settings.SERVICE_NAME,
    verison=settings.SERVICE_NAME,
    openapi_tags=tags_metadata
)


'''
    Fast API Middleware
'''
service.add_middleware(
    middleware.cors.CORSMiddleware,
    **middleware.cors.config
)

'''
    Fast API Router
'''
service.include_router(routers.users.router)
service.include_router(routers.items.router)
service.include_router(routers.health.router)


'''
    Fast API GraphQL Router
'''

routers.users.add_graphql_route(service)
