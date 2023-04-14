#!/usr/bin/python3
"""
THis module contains a function that loads
a json file and return a python
object
"""


def load_from_json_file(filename):
    """loads a json file and return
    a python object
    """
    import json
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.loads(f.read())
