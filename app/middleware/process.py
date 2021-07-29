"""
@Author:
    Bart Kim

@Note:

"""
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
import time

from fastapi import Request
from app.settings import settings


def process_init(service):
    pass
    # @service.middleware("https")
    # async def add_process_time_header(request: Request, call_next):
    #     start_time = time.time()
    #     response = await call_next(request)
    #     process_time = time.time() - start_time

    #     response.headers["X-Process-Time"] = str(process_time)

    #     return response
