#!/usr/bin/python3
"""
module 101-locked_class
"""


class LockedClass:
    """
    locks out all other instances but first_name
    """
    __slots__ = 'first_name'
