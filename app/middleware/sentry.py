"""
@Author:
    Bart Kim 

@Note:

"""

import sentry_sdk


sentry_sdk.init(
    f"https://497760d8a4b8475aa23eb7778e993c40@o933155.ingest.sentry.io/5882228",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)
