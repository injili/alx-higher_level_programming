#!/usr/bin/python3
"""
module 3-to_json
a function that returns the JSON rep of an objective string
"""


def to_json_string(my_obj):
    """
    takes in an object returning it's JSON representation
    """
    import json

    return (json.dumps(my_obj))
