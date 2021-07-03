import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ESUME_DATABASE_URL = os.getenv('ESUME_DATABASE_URL')

engine = create_engine(
    ESUME_DATABASE_URL, 
    connect_args={}
)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()
