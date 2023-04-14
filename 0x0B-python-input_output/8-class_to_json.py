#!/usr/bin/python3
"""THis module contains a function that returns
a dict of the instance of the
class passed to it
"""


def class_to_json(obj):
    """a function that returns the dictionary description with
    simple data structure for JSON serialization of an object:
    """
    return obj.__dict__
