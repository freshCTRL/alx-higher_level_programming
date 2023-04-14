#!/usr/bin/python3
"""
THis function adds  all arguments to a Python list,
and then save them to a file: save_to_json_file
load_from_json_file saved as a JSON representation
"""


def load_from_json_file(filename):
    """loads a json file and return
    a python object
    """
    import json
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())


def save_to_json_file(my_obj, filename):
    """takes a python object
    and convert to a json file
    """
    import json
    json_str = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(json_str)


def sumAllArgs():
    """a function that adds all command
    line arguments to a list
    """
    import json
    from sys import argv
    my_list = []
    count = len(argv)
    i = 1
    while i < count:
        my_list.append(argv[i])
        i += 1

    save_to_json_file(my_list, "add_item.json")
    load_from_json_file("add_item.json")
