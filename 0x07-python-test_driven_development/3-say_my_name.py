#!/usr/bin/python3
"""
Module 3-say_my_name
A function that prints my name
"""


def say_my_name(first_name, last_name=""):
    """
    A function that says my name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
