#!/usr/bin/python3
"""
module 4-from_json_string
a function that ruturns an object rep by a JSON string
"""


def from_json_string(my_str):
    """
    needs importation of json
    """
    import json

    return (json.loads(my_str))
