#!/usr/bin/python3
"""
This module
contains the
Base class
"""


class Base:
    """
    a base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises the base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a function that that returns the JSON string
        representation of list_dictionaries:
        """
        import json
        if len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """a function that writes the JSON string representation
        of list_objs to a file:
        """
        a_string = cls.to_json_string(list_objs)
        with open(__class__.__name__.json, mode="w", encoding="utf-8") as file:
            file.write(a_string)

    @staticmethod
    def from_json_string(json_string):
        """a function that returns a list of JSON
        string representation json_string
        """
        import json
        return json.loads(json_string)
