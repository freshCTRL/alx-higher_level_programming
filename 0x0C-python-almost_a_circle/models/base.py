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
        if list_dictionaries is None:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """a function that writes the JSON string representation
        of list_objs to a file:
        """
        import json
        a_string = cls.to_json_string(list_objs)
        b_string = json.loads(a_string)
        if not b_string:
            with open(__class__.__name__.json, mode="w", encoding="utf-8") as file:
                file.write(a_string)
        else:
            with open(__class__.__name__.json, mode="w", encoding="utf-8") as file:
                file.write(a_string)

    @staticmethod
    def from_json_string(json_string):
        """a function that returns a list of JSON
        string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        import json
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """a function  that returns an instance with
        all attributes already set:
        """
        dum = cls(width=1, height=1, x=0, y=0, id=None)
        return dum.update(**dictionary)

    @classmethod
    def load_from_file(cls):
        if not __class__.__name__.is_file():
            return []
        else:
            new_dict = cls.from_json_string(__class__.__name__.json)
            return cls.create(**new_dict)
