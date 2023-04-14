#!/usr/bin/python3
"""a BaseGeometry module
"""


class BaseGeometry:
    """a BaseGeometry class
    """

    def __init__(self):
        """Initialises the Base Class
        """
        self.value = None
        self.name = None

    def area(self):
        """Raises: Exception("area() is not implemented")
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value passed during init
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        self.name = name
        self.value = value
        return self.value


class Rectangle(BaseGeometry):
    """a Rectangle class that inherits
    from the BaseGeometry class
    """
    def __init__(self, width, height):
        """Initialises the Rectangle class
        """
        super().__init__()
        self.__width = BaseGeometry.integer_validator(self, self.name, width)
        self.__height = BaseGeometry.integer_validator(self, self.name, height)

    def area(self):
        """Calculate the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """always print when the print function or str method is called
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


class Square(Rectangle):
    """a Square class
    """
    width = 0
    height = 0

    def __init__(self, size):
        """Initialises the base class of Square.
        set the size of the square
        """
        width = height = size
        super().__init__(width, height)
        self.__size = BaseGeometry.integer_validator(self, self.name, size)

    def area(self):
        """Calculate the area of the Square
        """
        return self.__size ** 2
