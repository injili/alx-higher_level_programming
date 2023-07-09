#!/usr/bin/python3
"""
module 4-inherits_from.py
"""
def inherits_from(obj, a_class):
    """
    This function returns True if the object is an instance
    of a class that inherited from the specified class
    otherwise False

    Args
    obj: The object in comparison
    a_class: the parent class passed to the function
    """

    if type(obj) == a_class:
        return (False)
    elif isinstance(obj, a_class):
        return (True)
    else:
        return (False)
