#!/usr/bin/python3
"""
An integer addition function
The function takes in one or two integer or float values
Returns value or error depending on the input
"""

def add_integer(a, b=98):
    """Return the integer addition a and b
    Float values are accepted and cast into integers
    """
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
