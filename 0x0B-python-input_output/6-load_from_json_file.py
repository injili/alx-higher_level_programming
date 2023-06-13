#!/usr/bin/python3
"""
module 6-load_from_json_file
a function that creates an object
from a "JSON file"
"""



def load_from_json_file(filename):
    """
    open the file in read mode
    """
    import json

    with open(filename, mode="r") as f:
        return(f.read())
