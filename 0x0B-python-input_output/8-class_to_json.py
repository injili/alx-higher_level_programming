#!/usr/bin/python3
"""
module 8-class_to_json
a function that returns the dictionary description
with simple data structure for JSON serialization
of an object
"""


def class_to_json(obj):
    """
    returns the dictionary description
    Args:
        obj: the object passed to the function
    """
    return (obj.__dict__)
