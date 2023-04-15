#!/usr/bin/python3
"""
This module gets and update the list of command that are pass or
have been passed to command line argument, stores them inside a json file,
load them each time it needs to be updated
"""

from sys import argv
import json
import os
from pathlib import Path


def load_from_json_file(filename):
    """loads a json file and return
    a python object
    """
    import json
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.loads(f.read())


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to a text file,
    using a JSON representation:
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))


def main():
    """a script that adds all arguments to a Python list, and
    then save them to a file:
    """
    count = len(argv)

    i = 1
    my_list = []
    while i < count:
        d = argv[i]
        my_list.append(d)
        i += 1

    filename = "add_item.json"
    path = Path(filename)
    if not path.is_file():
        open(filename, "w")

    with open(filename, mode="r+", encoding="utf-8"):
        if os.stat(filename).st_size != 0:
            data = load_from_json_file(filename)
            data += my_list
            save_to_json_file(data, filename)
        else:
            save_to_json_file(my_list, filename)


main()
