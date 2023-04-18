#!/usr/bin/python3
"""
This module
contains the
Base class
"""


class Base:
    """
    a base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """
    a rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialises the Rectangle class
        """
        super().__init__()
        if id is not None:
            self.id = id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        retrieves the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width
        """
        self.__width = value

    @property
    def height(self):
        """
        retrieves the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets height
        """
        self.__height = value

    @property
    def x(self):
        """
        retrieves the x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets x
        """
        self.__x = value

    @property
    def y(self):
        """
        retrieves the y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets y
        """
        self.__y = value
