#!/usr/bin/python3
import json
"""
module 3-to_json
a function that returns the JSON rep of an objective string
"""


def to_json_string(my_obj):
    """
    takes in an object returning it's JSON representation
    """
    return (json.dumps(my_obj))
