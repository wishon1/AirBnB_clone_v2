#!/usr/bin/python3
""" module for the class review """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """ class Review whose attribute is inherited from BAseModel and Base"""
    if models.chosen_storage == 'db':
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """make initializion to Review"""
        super().__init__(*args, **kwargs)
