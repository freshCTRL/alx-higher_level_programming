#!/usr/bin/python3
"""
THis module contains a function that writes
an Object to a text file, using
a JSON representation:
"""


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to a text file,
    using a JSON representation:
    """
    import json
    json_str = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(json_str)
