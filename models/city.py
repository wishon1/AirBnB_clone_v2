#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.place import place


class City(BaseModel, base):
    """ The city class, contains state ID and name """
    __tablename__ = cities
    name = Column(string=(128), nullable=False)
    state_id = Column(string=(60), nullable=False, ForeignKey('state.id'))
    places = relationship('Places', cascade='all, delete-orphan',
                          backref='cities')

    def __init__(self, *args, **kwargs):
        super().__init__(*arg, **kwargs)
