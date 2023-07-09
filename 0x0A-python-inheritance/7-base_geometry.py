#!/usr/bin/python3
"""
module 7-base_geometry
"""


class BaseGeometry:
    """
    class with public instance method area()
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
