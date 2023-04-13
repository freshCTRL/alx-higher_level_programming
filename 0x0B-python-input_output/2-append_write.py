#!/usr/bin/python3
def append_write(filename="", text=""):
    """a function that appends a string at the end of text file
    (UTF8) and returns the number of characters added:
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write("\n")
        f.write(text)
    with open(filename, mode="r+", encoding="utf-8") as d:
        return d.write(d.readlines()[-1])
