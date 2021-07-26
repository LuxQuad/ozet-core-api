"""
@Author:
    Bart Kim 

@Note:

"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import settings

engine = create_engine(
    settings.ESUME_DATABASE_URL,
    connect_args={}
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()
