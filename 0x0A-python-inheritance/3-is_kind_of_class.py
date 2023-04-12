#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """a function that checks if an object is an
    instance of a class or of it subclass"""

    class lass(a_class):
        """a class lass which is a subclass
        of the class a_class
        """
        def __init__(self):
            pass

    sll = lass()
    if isinstance(obj, a_class) or isinstance(obj, type(sll)):
        return True
    return False
