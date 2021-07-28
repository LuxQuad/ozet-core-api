"""
@Author:
    Bart Kim 

@Note:

"""
from dataclasses import dataclass, field
from typing import List, Optional

from pydantic import BaseModel

from .item import Item


class Token(BaseModel):
    id: int
    key: str


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    #items: List(Item)

    class Config:
        orm_mode = True
