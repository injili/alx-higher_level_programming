#!/usr/bin/python3
"""
module 0-read_file
A function that reads a text
prints out to stout
"""


def read_file(filename=""):
    """
    opens a text file reading it
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
