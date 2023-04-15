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

    def integer_validator(self, name="", value=0):
        """validates the name
        and value passed
        """
        if type(value) != int:
            raise TypeError(str(name) + " " + "must be an integer")
        if value <= 0:
            raise ValueError(str(name) + " " + "must be greater than 0")
