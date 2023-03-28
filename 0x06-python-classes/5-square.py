#!/usr/bin/python3
class Square:

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def my_print(self):
        if self.__size != 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()
