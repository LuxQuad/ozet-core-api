"""
@Author:
    Bart Kim 

@Note:

"""
import os
from dotenv import load_dotenv

from pydantic import BaseSettings

'''
    Load Environments
'''
load_dotenv(verbose=True)


class Settings(BaseSettings):
    SENTRY_ENABLE: bool = os.getenv('ESUME_DATABASE_URL')
    SENTRY_DSN: str = os.getenv('ESUME_DATABASE_URL')

    SERVICE_NAME: str = os.getenv('SERVICE_NAME')
    SERVICE_DESC: str = os.getenv('SERVICE_DESC')
    SERVICE_VERSION: str = os.getenv('SERVICE_VERSION')

    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM')

    X_TOKEN: str = os.getenv('X_TOKEN')
    TOKEN: str = os.getenv('TOKEN')

    ESUME_DATABASE_URL: str = os.getenv('ESUME_DATABASE_URL')


settings = Settings()
