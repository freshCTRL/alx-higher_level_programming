#!/usr/bin/python3
"""This module contains a function that add two integers(a and b).
if a float is passed as an argument it cast it into an int.
if a or b is not an integer it raises a TypeError.
"""


def add_integer(a, b=98):
    """a function that adds two numbers.
    Raises: TypeError("if argument passed is not an integer")
    """
    if type(a) == float:
        if a + 1 == a:
            raise OverflowError("Float overflow")
        a = int(a)
    if type(b) == float:
        if b + 1 == b:
            raise OverflowError("Float overflow")
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a+b
