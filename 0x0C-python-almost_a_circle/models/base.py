#!/usr/bin/python3
"""
module base
the base of all other classes on this project
"""


import json

class Base:
    """
    This is the base class to evey other class

    Args:
        id(int): id passesd to the class
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))
