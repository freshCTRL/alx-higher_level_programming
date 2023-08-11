#!/usr/bin/python3
"""
    This module
    contains the
    Base class
"""
import csv
import json
"""
    importing json
    importing csv
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
        """
            a function that that returns the JSON string
            representation of list_dictionaries:
        """
        import json
        if list_dictionaries is None:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            a function that writes the JSON string representation
            of list_objs to a file:
        """
        if list_objs is None:
            a_string = cls.to_json_string([])
        elif len(list_objs) == 0:
            a_string = cls.to_json_string([])
        else:
            new_list = [obj.to_dictionary() for obj in list_objs]
            a_string = cls.to_json_string(new_list)
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as file:
            file.write(a_string)

    @staticmethod
    def from_json_string(json_string):
        """
            a function that returns a list of JSON
            string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            a function  that returns an instance with
            all attributes already set:
        """
        if f"{cls.__name__}" != "Square":
            dum = cls(width=1, height=1, x=0, y=0, id=None)
            dum.update(**dictionary)
        else:
            dum = cls(size=1, x=0, y=0, id=None)
            dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """
            a function that returns a list of instances:
        """
        import os
        filename = f"{cls.__name__}.json"
        if not os.path.isfile(filename):
            return []
        else:
            with open(filename, mode="r", encoding="utf-8") as f:
                content = f.read()
            ls = cls.from_json_string(content)

            return [cls.create(**item) for item in ls]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            a function that writes object(dictionaries)
            of list_objs to a csv file:
        """
        head = []
        if list_objs is not None:
            if len(list_objs) != 0:
                new_list = [obj.to_dictionary() for obj in list_objs]
                head = new_list[0].keys()
            else:
                new_list = []
        else:
            new_list = []
        with open(f"{cls.__name__}.csv", mode="w", newline="") as f:
            csv_writer = csv.DictWriter(f, fieldnames=head)
            if new_list:
                csv_writer.writeheader()
                csv_writer.writerows(new_list)
            else:
                csv_writer.writerows([])

    @classmethod
    def load_from_file_csv(cls):
        """
            a function that pulls object(dictionaries)
            of list_objs from a csv file:
        """
        import os
        filename = f"{cls.__name__}.csv"
        if not os.path.isfile(filename):
            return []
        else:
            with open(filename, mode="r", encoding="utf-8") as csvFile:
                csv_reader = csv.DictReader(csvFile)
                ls = [itm for itm in csv_reader]

        for obj in ls:
            for key, values in obj.items():
                obj[key] = int(values)

        return [cls.create(**item) for item in ls]
