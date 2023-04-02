#!/usr/bin/python3
"""square module.

THis module take size of a square and calculate the square
it takes the position parsed and position the square

"""


class Square:
    """square class

    """

    def __init__(self, size=0, position=(0, 0)):
        """initialises the square.
        Args:
            size: length of side of the square
            position: position of the square

        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """retrieve the size property of a square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """set the size property of a square

        Raises:
            TypeError: if size is not an integer
            ValueError: If size < 0

        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieve the position property of a square

        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the position property of a square

        """

        if type(value) != tuple:
            raise TypeError("position must be a
                            tuple of 2 positive integers")
        else:
            if len(value) != 2:
                raise TypeError("position must be a
                                tuple of 2 positive integers")
            else:
                for i in value:
                    if type(i) != int:
                        raise TypeError("position must be a
                                        tuple of 2 positive integers")
                    if i < 0:
                        raise TypeError("position must be a
                                        tuple of 2 positive integers")
            self.__position = value

    def area(self):
        """Calculate the area of a square

        """
        return self.__size ** 2

    def my_print(self):
        """prints the square in #'s and sets position like coordinates

        """

        if self.__size != 0:
            if self.__position[1] == 0:
                for x in range(self.__size):
                    print("{}{}".format(" " * self.position[0],
                          self.__size * "#"))
            else:
                for s in range(self.position[1]):
                    print()
                for x in range(self.__size):
                    print("{}{}".format(" " * self.position[0],
                          self.__size * "#"))
        else:
            print()
