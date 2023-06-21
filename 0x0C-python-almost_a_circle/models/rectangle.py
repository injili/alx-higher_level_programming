#!/usr/bin/python3
"""
module rectangle
inherits from the class Base
"""


from models.base import Base


class Rectangle(Base):
    """
    an instanciation of the class rectangle

    Args:
        width(int): the width of rectangle
        height(int): the height of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """intialize"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for i in range(self.__height)))

    def __str__(self):
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.__class__.__name__, self.id, self.__x, self.__y,
                self.__width, self.__height)

    def update(self, *args, **kwargs):
        if args:
            k = 0
            for value in args:
                if k == 0:
                    self.id = value
                elif k == 1:
                    self.width = value
                elif k == 2:
                    self.height = value
                elif k == 3:
                    self.x = value
                else:
                    self.y = value
                k += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        di = {}
        di["id"] = self.id
        di["width"] = self.width
        di["height"] = self.height
        di["x"] = self.x
        di["y"] = self.y
        return (di)
