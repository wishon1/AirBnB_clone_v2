#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String
from models.place import Place
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """inherits from BaseModel and Base"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship('place', secondary='place_amenity')
