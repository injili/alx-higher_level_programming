#!/usr/bin/python3
"""
module 4-rectangle
a class that defines a rectangle
"""


class Rectangle:
    """
    A class that defines a rectangle

    Args:
        width(int): the width of the rectangle
        height(int): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """get the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """get the width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        result = ''
        if self.__width == 0 or self.__height == 0:
            return (result)
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    result += '#'
                if (i + 1 < self.__height):
                    result += '\n'
            return (result)

    def __repr__(self):
        """return a string representation of the string"""
        return (f"Rectangle({self.width}, {self.height})")

    def __del__:
        print(f"Bye rectangle...")
