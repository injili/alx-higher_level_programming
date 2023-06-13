#!/usr/bin/python3
"""
module 6-load_from_json_file
a function that creates an object
from a "JSON file"
"""


def load_from_json_file(filename):
    """
    Create python obj from JSON file
    Args:
        filename: the json file
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return (json.load(f))
