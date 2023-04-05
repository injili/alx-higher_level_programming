#!/usr/bin/python3
"""defines a class and finds the area"""


class Square:
    """instantation of the class."""
    def __init__(self, size=0):
        """private instance attribute."""
        self.__size = size

        if type(self.__size) != int:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """public instance to get the area"""
        return self.__size * self.__size
