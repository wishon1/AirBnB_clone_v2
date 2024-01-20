#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """
        The city class, contains state ID and name
        Args:
            BaseModel: BaseModel class inherited from base_model.py
            base: class inherited
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
    places = relationship('Places', cascade='all, delete-orphan',
                          backref='cities')

    def __init__(self, *args, **kwargs):
        super().__init__(*arg, **kwargs)
