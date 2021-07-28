"""
@Author:
    Bart Kim 

@Note:

"""

import sentry_sdk
from app.settings import settings


def sentry_init():
    sentry_sdk.init(
        f"{settings.SENTRY_DSN}",

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0
    )
