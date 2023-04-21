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
        width = height = size
        super().__init__(width, height, x=0, y=0, id=None)

    def __str__(self):
        """
        gets called when the str or print method is called
        """
        return "[Square]" + " " + "(" + str(self.id) + ")" + " " + str(self.x)\
            + "/" + str(self.y) + " " + "-" + " " + str(self.width)

    @property
    def size(self):
        """
        retrieves the size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets size
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        size = value
        width = height = size
        super().__init__(width, height, x=0, y=0, id=None)

    def update(self, *args, **kwargs):
        """This function update the class Square by assigning
        to attributes
        """
        if len(args) != 0:
            if type(args[0]) != dict:
                try:
                    self.width = args[0]
                    self.height = args[0]
                    self.x = args[1]
                    self.y = args[2]
                    self.id = args[3]
                except IndexError:
                    return
        else:
            if type(kwargs) == dict:
                for key, value in kwargs.items():
                    if key == "size":
                        self.width = kwargs[key]
                        self.width = kwargs[key]
                    if key == "x":
                        self.x = kwargs[key]
                    if key == "y":
                        self.y = kwargs[key]
                    if key == "id":
                        self.id = kwargs[key]
            else:
                for key in kwargs:
                    if key == "id":
                        self.id = kwargs[key]
                    if key == "size":
                        self.id = kwargs[key]
                    if key == "x":
                        self.x = kwargs[key]
                    if key == "y":
                        self.y = kwargs[key]
