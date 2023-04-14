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
