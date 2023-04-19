#!/usr/bin/python3
"""
a BaseGeometry module
containing a method that determines
the value of area of the geometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits
    from a subclass rectangle
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        width = height = size
        super().__init__(width, height)
        """Initialises the Square
        class
        """
        self.__size = size

    def area(self):
        """the function that returns the area
        of a square"""
        return self.__size ** 2
