#!/usr/bin/python3
"""
module 2-append_write
a function that appends a string to the end of the text file
returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    opens the file in append mode
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
