#!/usr/bin/python3
"""a rectangle Module

"""


class Rectangle:
    """a rectangle class
    """

    def __init__(self, width=0, height=0):
        """Initialises a rectangle class.
        Args:
            width: stores the width of the rectangle
            height: stores the height of the rectangle

        Raises 1:
            TypeError: if width is not an integer
            ValueError: if width is not >= 0

        Raises 2:
            TypeError: if height is not an integer
            ValueError: if height is not >= 0
        
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        
        if type(height) != int:
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("width must be >= 0")
        self.__height = height

    @property
    def width(self):
        """retrieves the width property of a rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width property of a rectangle.

        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height property of a rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """set the height property of a rectangle.

        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
