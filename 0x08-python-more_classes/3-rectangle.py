#!/usr/bin/python3
"""a Rectangle Module

"""


class Rectangle:
    """a Rectangle class

    """

    def __init__(self, width=0, height=0):
        """Initialises a Rectangle class
        Args:
            width: stores the width of the rectangle
            height: stores the height of the rectangle

        """

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """retrieves the value of width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of the height of a rectangle
        Raises:
            TypeError:
            ValueError:

        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the value of height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of the height
        Raises:
            TypeError:
            ValueError:

        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of a rectangle

        """

        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of a rectangle

        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """the function goes in here when it is call
        with a print function or str

        """

        a = []
        for i in range(self.width):
            a.append('#')
        a.append("\n")
        b = "".join(a)
        return self.__height * b
