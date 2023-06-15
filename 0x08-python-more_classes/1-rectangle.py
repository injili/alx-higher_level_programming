#!/usr/bin/python3
"""
module 1-rectabgle
"""


class Rectangle:
    """define the class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height= height

    """property"""
    def width(self):
        return (self.__width)

    """property setter"""
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    """property"""
    def height(self):
        return (self.__height)

    """property setter"""
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value
