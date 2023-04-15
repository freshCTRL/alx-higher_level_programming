#!/usr/bin/python3
"""THis module contains a function that returns
true if the object is an instance of a class
that is inherited for the specified class otherwise
false
"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance of a
    class that inherited from the specified class ; otherwise False
    """
    for i in a_class.__subclasses__():
        if isinstance(obj, i):
            return True
    return False
