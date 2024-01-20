#!/usr/bin/python3
"""
This module contains unit tests for the HBNBCommand class in the
console (command interpreter).
"""
import json
import MySQLdb
import os
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City


class TestHBNBCommand(unittest.TestCase):
    """
    Test class for the HBNBCommand class.
    """

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_create_city(self):
        """
        Tests the create command with file storage for the City class.
        """
        console_instance = HBNBCommand()

        # First test case
        initial_count = len(storage.all(City).keys())
        console_instance.onecmd('create City name="Texas"')
        updated_count_1 = len(storage.all(City).keys())
        self.assertEqual(updated_count_1, initial_count + 1)

        # Second test case
        updated_count_2 = len(storage.all(City).keys())
        console_instance.onecmd('create City name="NewYork"')
        updated_count_3 = len(storage.all(City).keys())
        self.assertEqual(updated_count_3, updated_count_2 + 1)

        # Third test case
        counter = 0
        city_element = None
        for element, value in storage.all(City).items():
            counter += 1
            if counter == updated_count_3:
                city_element = value
        self.assertEqual('NewYork', city_element.__dict__["name"])
