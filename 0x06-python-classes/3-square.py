#!/usr/bin/python3
"""square module"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """initialises the square.
        Args:
            size: length of side of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: If size < 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of a square"""
        return self.__size ** 2
