#!/usr/bin/python3
"""
Module 0-add_integer
Function add_integer takes int or float values
Returns an int sum
"""


def add_integer(a, b=98):
    """
    Returns a + b
    """
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
