#!/usr/bin/python3
"""
This module
contains the
Base class
"""

from models.base import Base
"""
imports from parent class Base
"""


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
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        return the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """that prints in stdout the Rectangle instance
        with the character #
        """
        for i in range(self.height):
            if i != self.__height:
                print("{}".format(self.__width * '#'))

    def __str__(self):
        """a function that gets called when
        the str builtin or print is called
        """
        return "[Rectangle]" + " " + "(" + str(self.id) + ")" + " "\
            + str(self.__x) + "/" + str(self.__y) + " " + "-" + " "\
            + str(self.__width) + "/" + str(self.__height)
