"""
@Author:
    Bart Kim 

@Note:

"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import esume_base


class Jet(esume_base):
    __tablename__ = "jets"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
