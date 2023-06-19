#!/usr/bin/python3
"""
unittest for Rectangle class
# run with the command python -m unittest discover tests
# run wth python -m unittest tests/test_models/test_rectangle.py
"""


import unittest
import pep8
import models.rectangle
from io import StringIO
from contextlib import redirect_stdout

class TestPep8(unittest.TestCase):
    """Pep8 models/rectangle.py and tests/test_modules/test_rectangle.py"""
    def test_pep8(self):
        """pep8"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
