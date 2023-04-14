#!/usr/bin/python3
"""
THis module contains a function that appends a
string at the end of text file (UTF8) and
returns the number of characters added:
"""


def to_json_string(my_obj):
    """a function that returns the JSON representation
    of an object (string):
    """
    import json
    return json.dumps(my_obj)
