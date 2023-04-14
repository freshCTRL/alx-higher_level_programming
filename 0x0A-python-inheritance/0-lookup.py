#!/usr/bin/python3
"""
THis module contains a file that function
that returns the list of available
attributes and methods of an object:
"""


def lookup(obj):
    """function that returns the list of available
    attributes and methods of an object:
    """
    return dir(obj)
