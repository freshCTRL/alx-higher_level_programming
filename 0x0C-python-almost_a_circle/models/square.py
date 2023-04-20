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
        if len(args) != 0:
            if type(args[0]) != dict:
                if len(args) == 1:
                    self.id = args[0]
                if len(args) == 2:
                    self.id = args[0]
                    self.width = self.height = args[1]
                if len(args) == 3:
                    self.id = args[0]
                    self.width = self.height = args[1]
                    self.x = args[2]
                if len(args) == 4:
                    self.id = args[0]
                    self.width = self.height = args[1]
                    self.x = args[2]
                    self.y = args[3]
            else:
                for key in kwargs:
                    if key == "id":
                        self.id = kwargs[key]
                    if key == "size":
                        self.width = self.height = kwargs[key]
                    if key == "x":
                        self.x = kwargs[key]
                    if key == "y":
                        self.y = kwargs[key]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "size":
                    self.width = self.height = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]
