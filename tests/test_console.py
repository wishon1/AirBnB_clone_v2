#!/usr/bin/python3
""" test module for the console file"""
import os
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
from models.base_model import BaseModel
from models.user import User

class TestHBNBCommand(unittest.TestCase):
    """ tests cases for the console """
    def capture_output(self, command):
        """ capture the ouput in str format """
        with patch('sys.stdout', new_callable=StringIO) as expected_std:
            console = HBNBCommand()
            self.console.onecmd(command)
            return expected_std.getvalue().strip()

    def test_create_command(self):
        """ test cases for the do_create() method """
        # Test case 1: valid string parameter
        cmd = 'create State name="California"'
        output = self.capture_output(cmd)
        self.assertIn('California', output)
        
        # test if object creation was sucessful
        state_instance = storage.get("State", output.split()[1])
        self.assertIsNotNone(state_instance)
        self.assertEqual(state_instance.name, 'California')

        # Test case 2: string with special characters
        cmd = 'create State name="My\Little_\_house"'
        output = self.capture_output(cmd)
        self.assertIn('My Little house', output)

        state_instance = storage.get("State", output.split()[1])
        self.assertIsNotNone(state_instance)
        self.assertEqual(state_instance.name, 'My Little house')

        # Test case 4: integer parameter
        cmd = 'create State name=32'
        output = self.capture_output(cmd)
        self.assertIn('32', output)

        # Test case 5: decimal parameter
        cmd = 'create State name=3.147'
        output = self.capture_output(cmd)
        self.assertIn('3.147', output)

        # Test case 6: missing class name
        cmd = 'create'
        output = self.capture_output(cmd)
        self.assertEqual(output, "** class name missing **")

        # Test case 7: non-existent class name
        cmd = 'create NonExistentClass name="Test"'
        output = self.capture_output(cmd)
        self.assertIn('** class doesn\'t exist **', output)
        self.assertIsNone(storage.get("NonExistentClass"))
