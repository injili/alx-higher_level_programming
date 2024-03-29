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
        id(int): id passed to the class
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

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            json_string = []
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
            filename = cls.__name__ + ".json"
            with open(filename, "w") as f:
                f.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + ".json"
        the_list = []
        try:
            with open(file_name, "r", newline='') as f:
                instance = cls.from_json_string(f.read())
            for i, k in enumerate(instance):
                the_list.append(cls.create(**instance[i]))
        except:
            pass
        return (the_list)
