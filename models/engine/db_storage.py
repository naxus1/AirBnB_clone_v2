#!/usr/bin/python3
"""The engine of alchemy to conect the mysql
"""

from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
HBNB_ENV = getenv('HBNB_ENV')


class DBStorage():
    """ the clase like filestorage but with database alchemy
    """

    __engine = None
    __session = None
    all_classes = [City, State, User, Place, Review, Amenity]

    def __init__(self):
        """ the init method to start the engine db
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST, HBNB_MYSQL_DB,
                                             pool_pre_ping=True))
        metadata = MetaData()
        if HBNB_ENV == "test":
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ bring all the clases from the database acoord to the cls type
        """
        dictionary = {}
        if cls:
            data = self.__session.query(cls).all()
            ke = cls.__name__ + "."
            for obj in data:
                dictionary[ke + obj.id] = obj
            return dictionary
        else:
            for clase in self.all_classes:
                data = self.__session.query(clase).all()
                ke = clase.__name__ + "."
                for obj in data:
                    dictionary[ke + obj.id] = obj
            return dictionary

    def new(self, obj):
        """  add the object to the current database session (self.__session)
        """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """  delete from the current database session obj if not None
        """
        if obj:
            clase = type(obj)
            borrar = self.__session.query(clase).filter(clase.id.like(obj.id))
            session.delete(borrar)
            self.save()

    def reload(self):
        """ create all tables in the database (feature of SQLAlchemy) create the
        current database session (self.__session) from the engine
        (self.__engine) by using a sessionmaker - the option expire_on_commit
        must be set to False ; and scoped_session - to make sure your Session
        is thread-safe
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))()
