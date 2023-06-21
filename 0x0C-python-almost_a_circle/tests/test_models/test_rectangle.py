#!/usr/bin/python3
"""
unittest for Rectangle class
# run with the command python -m unittest discover tests
# run wth python -m unittest tests/test_models/test_rectangle.py
"""


import os
import unittest
from models import rectangle
from io import StringIO
from contextlib import redirect_stdout
Rectangle = rectangle.Rectangle


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
            Rectangle(15, 25, 1, -4, 99)

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
        self.assertEqual(Rectangle(4, 5).area(), 20)
        self.assertEqual(Rectangle(15, 25, 1, 2, 99).area(), 375)
        self.assertEqual(Rectangle(3, 12, 1, 2).area(), 36)

    def test_the_print(self):
        out = "[Rectangle] (99) 1/2 - 15/25"
        self.assertEqual(str(Rectangle(15, 25, 1, 2, 99)), out)

    def test_the_dislay(self):
        with StringIO() as xept, redirect_stdout(xept):
            Rectangle(3, 4).display()
            x = xept.getvalue()
        self.assertEqual(x, '###\n###\n###\n###\n')
        with StringIO() as xept, redirect_stdout(xept):
            Rectangle(3, 4, 1, 2).display()
            x = xept.getvalue()
        self.assertEqual(x, '\n\n ###\n ###\n ###\n ###\n')

    def test_the_update(self):
        """test update with *args"""
        r = Rectangle(15, 25, 1, 2, 99)
        r.update(7, 7, 7, 7, 7)
        self.assertEqual(str(r), '[Rectangle] (7) 7/7 - 7/7')
        r.update()
        self.assertEqual(str(r), '[Rectangle] (7) 7/7 - 7/7')
        r.update(90)
        self.assertEqual(str(r), '[Rectangle] (90) 7/7 - 7/7')
        r.update(70, 10)
        self.assertEqual(str(r), '[Rectangle] (70) 7/7 - 10/7')
        r.update(80, 15, 20)
        self.assertEqual(str(r), '[Rectangle] (80) 7/7 - 15/20')
        r.update(99, 15, 25, 1)
        self.assertEqual(str(r), '[Rectangle] (99) 1/7 - 15/25')
        r.update(99, 15, 25, 1, 2)
        self.assertEqual(str(r), '[Rectangle] (99) 1/2 - 15/25')
        """test update fail cases"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(99, "width", 25, 1, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(99, 15, 25, -9, 4)
        """test update with **kwargs"""
        r1 = Rectangle(15, 25, 1, 2, 99)
        r1.update(id=9)
        self.assertEqual(str(r1), '[Rectangle] (9) 1/2 - 15/25')
        r1.update(width=7)
        self.assertEqual(str(r1), '[Rectangle] (9) 1/2 - 7/25')
        r1.update(height=4)
        self.assertEqual(str(r1), '[Rectangle] (9) 1/2 - 7/4')
        r1.update(x=8)
        self.assertEqual(str(r1), '[Rectangle] (9) 8/2 - 7/4')
        r1.update(y=19)
        self.assertEqual(str(r1), '[Rectangle] (9) 8/19 - 7/4')
        r1.update(id=99, width=14, height=24, x=1, y=2)
        self.assertEqual(str(r1), '[Rectangle] (99) 1/2 - 14/24')
        r1.update(invalid=12, twelve=8, x=900)
        self.assertEqual(str(r1), '[Rectangle] (99) 900/2 - 14/24')
