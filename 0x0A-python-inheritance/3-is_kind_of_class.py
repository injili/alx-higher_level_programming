#!/usr/bin/python3
"""
module 3-is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    this function returns True if the object is an instance of
    or if the object is an instance of a class that inherited from
    the specified class; otherwise False

    Args:
    obj: the object to be compared
    a_class: the class passed to the function
    """

    return (isinstance(obj, a_class))
