#!/usr/bin/python3
"""
module 6-max_integer
tests
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    run with python3 -m unittest -v tests/6-max_integer_test.py
    """
    def test_the_module_docstring(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_the_function_docstring(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)

    def test_signed_ints_and_floats(self):
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-1.5, -2, -3]), -1.5)
        self.assertEqual(max_integer([10, -10, 10]), 10)
        self.assertEqual(max_integer([{1, 9}, {3}, {4}]), {1, 9})

    def test_strings(self):
        self.assertEqual(max_integer("1279"), '9')
        self.assertEqual(max_integer("abyfz"), 'z')
        self.assertEqual(max_integer(['a', 'b', 'c', 'x']), 'x')
        self.assertEqual(max_integer(["wbn", 'z']), 'z')

    def test_lists(self):
        self.assertEqual(max_integer([[1, 3], [1, 1]]), [1, 3])

    def test_error_handling(self):
        with self.assertRaises
