"""
@Author:
    Bart Kim 

@Note:

"""
from dataclasses import dataclass, field
import email
from typing import List, Optional

from pydantic import BaseModel

from .item import Item


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserBase(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None


class User(UserBase):
    id: int
    is_active: Optional[bool] = None

    hashed_password: str

    items: List[Item]

    class Config:
        orm_mode = True


class UserInDB(UserBase):
    hashed_password: str


class UserCreate(UserBase):
    password: str = None
