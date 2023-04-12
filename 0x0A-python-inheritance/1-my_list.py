#!/usr/bin/python3
"""a Mylist module"""


class list:
    """a class named list
    """

    my_list = []

    def __init__(self):
        """Initialises the list class
        """
        list.my_list = []


class MyList(list):
    """a Class that inherit from list
    """
    def __init__(self):
        super().__init__()

    def append(self, value):
        """a function that append the value passed
        """
        list.my_list.append(value)

    def __str__(self):
        """always called when the str method is
        called or the print function
        """
        return str(list.my_list)

    def print_sorted():
        """a function that prints the list
        but sorted (ascending sort)
        """
        print(sorted(list.my_list))
