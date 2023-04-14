#!/usr/bin/python3
"""a module containing a student class and a function
that returns the dict of the instance to
the class or the class
"""


class Student:
    """a student
    class
    """
    def __init__(self, first_name, last_name, age):
        """Initialises the
        student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dict of the class
        or its instance(depends on what is call)
        """
        return self.__dict__
