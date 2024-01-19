#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import place
from models.review import Review
from os import getenv


chosen_storage = os.getenv('HBNB_TYPE_STORAGE', default='fs')

if chosen_storage == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
storage = FileStorage()
storage.reload()
