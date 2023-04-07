#!/usr/bin/python3
"""
This module contains a function that prints square in #'s
based on an input size, if size is not int, a TypeError exception
is raised else if size is < 0, ValueError exception is raised
"""


def print_square(size):
    """
    Raises: TypeError if size != int, ValueError if size < 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("{}".format(size * '#'))
