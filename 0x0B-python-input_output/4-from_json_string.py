#!/usr/bin/python3
"""
THis module contains a function function that returns
an object(Python data structure) represented by
a JSON string:
"""


def from_json_string(my_str):
    """ a function that returns an object(Python
    data structure) represented by a JSON string:
    """
    import json
    return json.loads(my_str)
