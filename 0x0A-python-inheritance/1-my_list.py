#!/usr/bin/python3
"""a Mylist module which has a subclass
Mylist and a parent class list.
it init an empty list, has append function and the
magic str method
"""


class list:
    """a class named list
    containing an empty list
    """
    def __init__(self):
        """Initialises the
        list class
        """
        self.list = []

    def append(self, value):
        """append to
        a list
        """
        self.list.append(value)

    def __str__(self):
        return str(self.list)


class MyList(list):
    """a Class that inherit
    from class list
    """
    def print_sorted(self):
        """a function that prints the list
        but sorted (ascending sort)
        """
        print(sorted(self.list))
