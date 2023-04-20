#!/usr/bin/python3
"""
THis module contains the class square and it inherits
functions of the class rectangle, it also import a
module containing the class rectangle
"""

from models.rectangle import Rectangle
"""this line import the class rectangle
from the models module
"""


class Square(Rectangle):
    """
    a Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialises the square class
        """
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size
        width = self.__size
        height = self.__size
        super().__init__(width, height, x=0, y=0, id=None)

    def __str__(self):
        """
        gets called when the str or print method is called
        """
        return "[Square]" + " " + "(" + str(self.id) + ")" + " " + str(self.x)\
            + "/" + str(self.y) + " " + "-" + " " + str(self.__size)

    @property
    def size(self):
        """
        retrieves the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets size
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
