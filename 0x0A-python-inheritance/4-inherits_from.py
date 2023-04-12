#!/usr/bin/python3

def inherits_from(obj, a_class):
    """a function that returns True if the
    object is an instance of a class that
    inherited (directly or indirectly) from
    the specified class ; otherwise False
    """

    class lass(a_class):
        """inherits the base class
        """

        def __init__(self):
            """initialises the lass class"""
            pass

    sll = lass()
    if isinstance(obj, a_class) or isinstance(obj, type(sll)):
        return True
    return False
