#!/usr/bin/python3
""" module for the database storage """
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.base_model import Base
from os import getenv
import sqlalchemy
import models

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """data storage class """
    __engine = None
    __session = None

    def __init__(self):
        """constructor for the database engine"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the current database session"""
        new_dict = {}
        for d_clss in classes:
            if cls is None or cls is classes[d_clss] or cls is d_clss:
                objects = self.__session.query(classes[d_clss])
                for obj in objects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """ add objects to the current database session"""
        self.session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.session.commit()

    def delete(self, obj=None):
        """delete the specified obj from the current db sesson if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                     expire_on_commit=False)
        self.__session = scoped_session(session_maker)

    def close(self):
        """clse the query """
        self.__session.remove()
