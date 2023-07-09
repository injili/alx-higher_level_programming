#!/usr/bin/python3
"""
module 2-is_same_class
"""


def is_same_class(obj, a_class):
    """
    a function that returns True if the object is
    exactly an instance of the specifird class;
    otherwise, False

    Args
    obj: the object passed to the class
    a_class: the class in comparison
    """

    return (type(obj) == a_class)
