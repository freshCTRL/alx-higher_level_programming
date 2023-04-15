#!/usr/bin/python3
"""THis module contains a function that checks
if an object is an instance of a class
or if it is
it subclass
"""


def is_kind_of_class(obj, a_class):
    """a function that checks if an object is an
    instance of a class or of it subclass
    """
    if isinstance(obj, a_class):
        return True
    for i in a_class.__subclasses__():
        if isinstance(obj, i):
            return True
    return False
