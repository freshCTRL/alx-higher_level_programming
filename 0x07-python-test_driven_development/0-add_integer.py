#!/usr/bin/python3
"""This module contains a function that add two integers(a and b),
if a float is passed as an argument it cast it into integer
if either of the two argument is a float, an integer equivalent is used
"""


def add_integer(a, b=98):
    """a function that adds two numbers.
    Raises: TypeError("if argument passed is not an integer")
    """

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    try:
        res = a + b
        return int(res)
    except:
        if type(a) != int:
            raise TypeError("a must be an integer")
        if type(b) != int:
            raise TypeError("b must be an integer")
