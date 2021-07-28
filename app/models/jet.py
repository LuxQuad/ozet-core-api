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

    # Identifyer
    id = Column(Integer, primary_key=True, index=True)

    # Relationship
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="items")
