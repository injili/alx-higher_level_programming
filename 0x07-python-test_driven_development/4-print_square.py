#!/usr/bin/python3
"""
Module 4-print_square
A function that prints a square
The function prints with #
"""


def print_square(size):
    """
    size is the length and width
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="" if j + 1 != size else "\n")
