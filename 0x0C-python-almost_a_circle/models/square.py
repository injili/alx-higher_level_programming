#!/usr/bin/python3
"""
module square
A class square that inherits from rectangle
"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """The square that's a child class
    Args:
        size(int): value of the width and height
        x(int): value of x passed to the class
        y(int): value of y passed to the class
        id: can be none
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return (self.size)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                self.__class__.__name__, self.id, self.x,
                self.y, self.width)
