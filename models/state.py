#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
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
                      nullable=False,
                      Foreignkey=('state_id'))

    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")
