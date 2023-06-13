#!/usr/bin/python3
"""
module 5-save_to_json_file
a function that writes an object to a text file
uses JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
    opens a file in write mode
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json_obj = json.dumps(my_obj)
        return (f.write(json_obj))
