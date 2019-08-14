#!/usr/bin/python3
"""This is the state class"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    _tablename__ = "states"

    name = Column(String(128),
                  nullable=False)

    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan")
    @property
    def cities(self):
        all_data = models.storage.all("City")
