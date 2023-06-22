#!/usr/bin/python3
"""
module models/base.py
test cases
"""

import os
import json
import unittest
import models.base
import base.rectangle
Base = base.Base
Rectangle = rectangle.Rectangle


class TestBase(unittest.TestCase):
    """Test everything on the base class"""
    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_class_called(self):
        self.assertTrue(Base(10), self.__class__ == Base)

    def test_passed_id(self):
        self.assertTrue(Base(90), self.id == 90)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-4), self.id == -4)

    def test_no_argument(self):
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_private_attribute_access(self):
        with self.assertRaises(AttributeError):
            print(Base.__nb__objects)
            print(Base.nb__objects)

    def test_invalid_arguments(self):
        with self.assertRaises(TypeError):
            Base(10, 10)
