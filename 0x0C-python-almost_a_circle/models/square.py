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
        width = height = size
        super().__init__(width, height, x, y, id)
        if id is not None:
            self.id = id

    def __str__(self):
        """
        gets called when the str or print method is called
        """
        return "[Square]" + " " + "(" + str(self.id) + ")" + " " + str(self.x)\
            + "/" + str(self.y) + " " + "-" + " " + str(self.width)
