"""
@Author:
    Bart Kim 

@Note:

"""
from typing import List, Optional

from pydantic import BaseModel
from graphene_pydantic import PydanticInputObjectType, PydanticObjectType


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
