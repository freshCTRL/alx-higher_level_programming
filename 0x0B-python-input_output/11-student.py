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

    def to_json(self, attrs=None):
        """returns a dict of the class or its instance
        (depends on what is call) based on attr(as keys)
        """
        if attrs is not None:
            s = {}
            for key, values in self.__dict__.items():
                for ky in attrs:
                    if key == ky:
                        s[key] = values
                    continue
            return s
        return self.__dict__

    def reload_from_json(self, json):
        """reload the caller(the class itself ar it instance)
        with a dict(named json in this instance)
        """
        s = {}
        for ky, valu in json.items():
            for key, values in self.__dict__.items():
                if key == ky:
                    s[key] = values
        return s
