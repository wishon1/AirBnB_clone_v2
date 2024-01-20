#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models
import sqlalchemy


class State(BaseModel):
    """
        State class:
            Args:
                BaseModel: class which is inherited from bas_model.py
    """
    if models.chosen_storage == 'db':
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if models.chosen_storage != 'db':
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
