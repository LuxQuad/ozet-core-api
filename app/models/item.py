"""
@Author:
    Bart Kim 

@Note:

"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import esume_base


class Item(esume_base):
    __tablename__ = "items"

    # Identifyer
    id = Column(Integer, primary_key=True, index=True)

    # Column
    title = Column(String, index=True)
    description = Column(String, index=True)

    # Relationship
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")
