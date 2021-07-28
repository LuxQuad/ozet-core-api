"""
@Author:
    Bart Kim 

@Note:

"""
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import esume_base

from .item import Item


class User(esume_base):
    __tablename__ = "users"

    # Identifyer
    id = Column(Integer, primary_key=True, index=True)

    # Column
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    is_active = Column(Boolean, default=True)

    # Relationship
    items = relationship(Item, back_populates="owner")
