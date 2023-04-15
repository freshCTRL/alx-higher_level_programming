#!/usr/bin/python3
"""
a BaseGeometry module
containing a method that determines
the value of area of the geometry
"""


class BaseGeometry:
    """a BaseGeometry
    class
    """
    def area(self):
        """
        checks if the argument needed to determine the area is passed
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the name
        and value passed
        """
        if type(value) != int:
            raise TypeError(str(name) + " " + "must be an integer")
        if value <= 0:
            raise ValueError(str(name) + " " + "must be greater than 0")


class Rectangle(BaseGeometry):
    """
    a Rectangle class: a subclass to BaseGeometry class
    """

    def __init__(self, width, height):
        """Initialises the Square
        class
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        checks if the argument needed to determine the area is passed
        """
        return self.__width * self.__height

    def __str__(self):
        """the magic that returns the below whenever
        str or print of the class is called
        """
        return "[Rectangle]" + " " + str(self.__width) + "/"\
            + str(self.__height)
