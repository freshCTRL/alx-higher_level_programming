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
        with the character # and position it base on x and y
        """
        for i in range(self.__y):
            print()
        for i in range(self.height):
            if i != self.__height:
                print("{}{}".format(self.__x * " ", self.__width * '#'))

    def __str__(self):
        """a function that gets called when
        the str builtin or print is called
        """
        return "[Rectangle]" + " " + "(" + str(self.id) + ")"\
            + " " + str(self.__x) + "/" + str(self.__y) + " " + "-"\
            + " " + str(self.__width) + "/" + str(self.__height)

    def update(self, *args, **kwargs):
        """a function that Update the class Rectangle
        by assigning an argument to each attribute
        """
        if len(args) != 0:
            if type(args[0]) != dict:
                if len(args) == 1:
                    self.id = args[0]
                elif len(args) == 2:
                    self.id = args[0]
                    self.__width = args[1]
                elif len(args) == 3:
                    self.id = args[0]
                    self.__width = args[1]
                    self.__height = args[2]
                elif len(args) == 4:
                    self.id = args[0]
                    self.__width = args[1]
                    self.__height = args[2]
                    self.__x = args[3]
                elif len(args) == 5:
                    self.id = args[0]
                    self.__width = args[1]
                    self.__height = args[2]
                    self.__x = args[3]
                    self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """a function that returns a dict representation
        of a class, or it's instance when called
        """
        keys = ["id", "width", "height", "x", "y"]
        d = {}
        for key in keys:
            d[key] = getattr(self, key)

        return d
