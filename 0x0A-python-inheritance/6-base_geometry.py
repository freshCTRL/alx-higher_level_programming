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
