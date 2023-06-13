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
    with open(filename, "r") as the_file:
        content = the_file.read()
        print(content)
