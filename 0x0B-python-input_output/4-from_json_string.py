#!/usr/bin/python3
def from_json_string(my_str):
    """ a function that returns an object (Python data structure)
    represented by a JSON string:
    """
    import json
    with open("mydata.json", "w", encoding="utf-8") as f:
        f.write(my_str)
    with open("mydata.json", "r", encoding="utf-8") as myFile:
        return json.loads(myFile.read())
