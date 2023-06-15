#!/usr/bin/python3
"""
module 1-rectabgle
"""


class Rectangle:
    """define the class"""
    def __init__(self, width=0, length=0):
        self.__width = width
        self.__length = length

    """property"""
    def width(self):
        return (self.__width)

    """property setter"""
    def width(self, value):
        if type(self.__width) != int:
            raise TypeError("width must be an integer")
        elif self.__width < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    """property"""
    def length(self):
        return (self.__length)

    """property setter"""
    def length(self, value):
        if type(self.__length) != int:
            raise TypeError("length must be an integer")
        elif self.__length < 0:
            raise ValueError("length must be >=0")
        else:
            self.__length = value
