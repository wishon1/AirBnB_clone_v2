#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.place import place


class State(BaseModel):
    """ State class """
    __tablename__ = states

    name = Column(string(128), nullable=False)
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
