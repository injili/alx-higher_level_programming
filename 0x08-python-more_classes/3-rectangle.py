#!/usr/bin/python3
"""
module 2-rectangle
Area and Perimeter
"""


class Rectangle:
    """
    defines the class Rectangle.

    Args:
        width(int): An int representation of the width.
        height(int): An int representation of the height.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the value of the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area"""
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        """draw the rectangle sir"""
        result = ''
        for _ in range(self.__height):
            result += '#' * self.__width + '\n'
        return (result)
