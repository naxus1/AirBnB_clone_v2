from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker



class DBStorage():

    self __engine = None
    self __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB,
                                             pool_pre_ping=True)
        metadata = db.MetaData()
