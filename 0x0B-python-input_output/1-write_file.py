#!/usr/bin/python3
"""
module 1-write_file
a function that writes a string to a text file
returns the number of characters
"""


def write_file(filename="", text=""):
    """
    open file in write mode
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
