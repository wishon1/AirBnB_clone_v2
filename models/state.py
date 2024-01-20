#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
import models


class State(BaseModel):
    """
        State class:
            Args:
                BaseModel: class which is inherited from bas_model.py
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """ Getter attribute that returns the list of City instances
            with state_id equals to the current State.id
        """
        from models import storage
        list_city = []
        cities = storage.all()
        for city in cities.value():
            if city.state_id == self.id:
                list_city.append(city)
        return list_city
