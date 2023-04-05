#!/usr/bin/python3
"""Third class of square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """receives an object and size"""
        self.__size = size

        if type(self.__size) != int:
            raise TypeError("size must be an integer")

        if self.__size < 0:
            raise ValueError("size must be >= 0")
