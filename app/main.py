"""
@Author:
    Bart Kim 

@Note:

"""
from fastapi import Depends, FastAPI, HTTPException
from fastapi_pagination import add_pagination
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.settings import settings
from app.database import esume_session_local, esume_engine, esume_base


from app import middleware
from app import routers


'''
    DB Migrate
'''
esume_base.metadata.create_all(bind=esume_engine)

print('DB Sync')

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

if settings.SENTRY_ENABLE:
    middleware.sentry.sentry_init()

'''
    Fast API Router
'''
service.include_router(routers.users.router)
service.include_router(routers.items.router)
service.include_router(routers.health.router)

if settings.SENTRY_ENABLE:
    service.include_router(routers.sentry.router)


'''
    Fast API Pagination Init
'''

add_pagination(service)
