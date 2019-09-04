#!/usr/bin/python3
"""This is the state class"""

import models
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

    cities = relationship('City',
                          cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        all_data = models.storage.all(models.City)
        data_city = []
        for key, value in all_data.items():
            if value.state_id == self.id:
                data_city.append(value)
        return data_city
