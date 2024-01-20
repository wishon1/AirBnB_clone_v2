#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
import sqlalchemy


class City(BaseModel, Base):
    """
        The city class, contains state ID and name
        Args:
            BaseModel: BaseModel class inherited from base_model.py
            base: class inherited
    """
    if models.chosen_storage == 'db':
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities')
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """ constructor"""
        super().__init__(*arg, **kwargs)
