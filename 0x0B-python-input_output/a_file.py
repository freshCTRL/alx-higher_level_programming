#!/usr/bin/python3
from sys import argv
import json


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

    count = len(argv)

    i = 1
    my_list = []
    while i < count:
        d = argv[i]
        my_list.append(d)
        i += 1

    filename = "add_item.json"
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)


main()
