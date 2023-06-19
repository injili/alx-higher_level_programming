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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
            filename = cls.__name__ + ".json"
            with open(filename, "w") as f:
                f.write(cls.to_json_string(objs))
