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


class Token(esume_base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="tokens")


class User(esume_base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    tokens = relationship(Token, back_populates="owner")
    items = relationship(Item, back_populates="owner")


class UserGraph(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )


class UserConnection(relay.Connection):

    class Meta:
        node = UserGraph
