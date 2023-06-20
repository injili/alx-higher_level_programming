#!/usr/bin/python3
"""
unittest for Rectangle class
# run with the command python -m unittest discover tests
# run wth python -m unittest tests/test_models/test_rectangle.py
"""


import os
import unittest
import pep8
from models import rectangle
from io import StringIO
from contextlib import redirect_stdout
rectangle = rectangle.Rectangle

class TestPep8(unittest.TestCase):
    """Pep8 models/rectangle.py and tests/test_modules/test_rectangle.py"""
    def test_pep8(self):
        """pep8"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Fix Pep8')

class TestBase(unittest.TestCase):
    """tests for the module models/rectangle"""

    def test_all_attributes_given(self):
        """Test all the attributes match"""
        r1 = Rectangle(15, 25, 1, 2, 99)
        self.assertTrue(r1.width == 15)
        self.assertTrue(r1.height == 25)
        self.assertTrue(r1.x == 1)
        self.assertTrue(r1.y == 2)
        self.assertTrue(r1.id == 99)

    def test_default_attributes(self):
        """Test default attributes"""
        r2 = Rectangle(10, 20)
        self.assertTrue(r2.width == 10)
        self.assertTrue(r2.height == 20)
        self.assertTrue(r2.x == 0)
        self.assertTrue(r2.y == 0)
        self.assertTrue(r2.id is not None)

    def 
