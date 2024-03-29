#!/usr/bin/python3
"""
    THis module contains the class square and it inherits
    functions of the class rectangle, it also import
    a module containing the class rectangle
"""

from models.rectangle import Rectangle
"""
    this line import the class rectangle
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
        super().__init__(width, height, x, y, id)

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
        setattr(self, "width", value)
        setattr(self, "height", value)

    def update(self, *args, **kwargs):
        """
            This function update the class Square by assigning
            to attributes
        """
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            a function that returns a dict representation
            of a class, or it's instance when called
        """
        keys = ["id", "size", "x", "y"]
        d = {}
        for key in keys:
            d[key] = getattr(self, key)

        return d
