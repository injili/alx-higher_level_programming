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
    def test_class(self):
        self.assertEqual(type(Rectangle(15, 25)), Rectangle)

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

    def test_attribute_validation(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("15", 25, 1, 2, 99)
            Rectangle([15, 10], 25, 1, 2, 99)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(15, "25", 1, 2, 99)
            Rectangle(15, [25, 10], 1, 2, 99)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(15, 25, "1", 2, 99)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(15, 25, 1, "2", 99)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 25, 1, 2, 99)
            Rectangle(-4, 25, 1, 2, 99)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(15, 0, 1, 2, 99)
            Rectangle(15, -4, 1, 2, 99)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(15, 25, -4, 2, 99)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(15, 25, 1, -4, 99)i

    def test_private_attribute_access(self):
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(15, 25, 1, 2, 99, 90)
        with self.assertRaises(TypeError):
            Rectangle(15)
            Rectangle()
            Rectangle(None)

    def test_the_area(self):
        self.
