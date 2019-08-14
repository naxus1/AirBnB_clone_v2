#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'

    name = Column(String(128),
                  nullable=False)

    state_id = Column(String(60),
                      ForeignKey('state_id'), nullable=False)

    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")
