#!/usr/bin/python3
"""This module contains a function that add two integers(a and b),
if a float is passed as an argument it cast it into an int
if a is not an integer it raises a TypeError
if b is not and integer it raises a TypeError
"""


def add_integer(a, b=98):
    """Raises:
    TypeError: if argument passed is not an integer
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
