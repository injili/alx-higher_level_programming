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
        return (self.width)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                self.__class__.__name__, self.id, self.x,
                self.y, self.width)

    def update(self, *args, **kwargs):
        if args:
            k = 0
            for value in args:
                if k == 0:
                    self.id = value
                elif k == 1:
                    self.size = value
                elif k == 2:
                    self.x = value
                else:
                    self.y = value
                k += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
