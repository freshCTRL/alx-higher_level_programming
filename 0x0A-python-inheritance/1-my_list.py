#!/usr/bin/python3
"""a Mylist module"""


class list:
    """a class named list
    """

    my_list = []

    def __init__(self):
        """Initialises the list class
        """
        pass


class MyList(list):
    """a Class that inherit from list
    """

    def append(self, value):
        """a function that append the value passed
        """
        super().my_list.append(value)

    def __str__(self):
        """always called when the str method is
        called or the print function
        """
        return str(MyList.my_list)

    @staticmethod
    def print_sorted():
        """a function that prints the list
        but sorted (ascending sort)
        """
        print(sorted(MyList.my_list))
