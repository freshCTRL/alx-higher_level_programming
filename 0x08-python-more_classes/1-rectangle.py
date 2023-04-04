#!/usr/bin/python3
"""a Rectangle Module

"""


class Rectangle:
    """a Rectangle class

    """

    def __init__(self, width=0, height=0):
        """initialises the Rectangle.
        Args:
            width: stores the width of a rectangle
            height: stores the height of a rectangle

        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve the width property of a rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width property of a rectangle
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0

        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height property of a rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """set the height property of a rectangle
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0

        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of a rectangle

        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of a rectangle

        """

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
