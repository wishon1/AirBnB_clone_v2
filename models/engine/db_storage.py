#!/usr/bin/python3
""" module for the database storage """
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.base_model import Base
from os import getenv


class DBStorage:
    """data storage class """
    __engine = None
    __session = None

    def __init__(self):
        """constructor for the database engine"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self._engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                     .format(user, password, host, db),
                                     pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query the current database sesson"""
        class_names = (Amenity, City, Place, Review, State, User)
        value = dict()

        if cls is None:
            for item in class_names:
                query = self.__session.query(item)
                for obj in query.all():
                    value_Key = '{}.{}'.format(obj.__class__.name__, obj.id)
                    value[value_Key] = obj
        else:
            query = self.session.query(cls)
            for obj in query.all():
                obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                value[value_key] = obj
        return value

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
        self.__session = session_maker()

    def close(self):
        """clse the query """
        self.__session.close()
