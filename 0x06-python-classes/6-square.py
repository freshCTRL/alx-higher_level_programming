#!/usr/bin/python3
"""square module"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialises the square.
        Args:
            size: length of side of the square
            position: position of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: If size < 0
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Calculate the area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """retrieve the size property of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size property of a square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieve the position property of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position property of a square"""
        if type(value) != tuple or len(value) != 2 or \
                type(value[0]) != int or type(value[1]) != int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the square in #'s"""
        if self.__size != 0:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
