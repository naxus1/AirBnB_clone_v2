#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
import models
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False),
                      Column('amenity_id', String(60), ForeignKey
                             ('amenities.id'), nullable=False))

class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', backref='place')
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False, backref='place_amenities')

    @property
    def reviews(self):
        """ get the reviews to filestorage option """
        comentarios = []
        all_data = models.storage.all(models.Review)
        for key, value in all_data.items():
            if value.place_id == self.id:
                comentarios.append(value)
        return comentarios

    @property
    def amenities(self):
        """ get the amenities """
        comodidades = []
        all_data = models.storage.all(models.Amenity)
        for key, value in all_data.items():
            for amenity in self.amenity_ids:
                if value.id == amenity:
                    comodidades.append(value.id)
        return comodidades

    @amenities.setter
    def amenities(self, obj):
        """ set the amenities ids """
        if type(obj) is Amenity:
            amenity_ids.append(obj.id)
