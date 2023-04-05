#!/usr/bin/python3
"""defines a class and finds the area"""


class Square:
    """instantation of slass."""
    def __init__(self, size=0, position):
        """private instance attributes"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieves the value of size"""
        return self.__size

    @property
    def position(self):
        """retrieves the value os position"""
        return self.__position

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @position.setter
    def position(self, value):
        """set the values of the position attribute"""
        isinstance(vslue tuple):

    def area(self):
        """retrieve the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints out the square"""
        for i in range(self.__size):
            [print("#", end="")for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

