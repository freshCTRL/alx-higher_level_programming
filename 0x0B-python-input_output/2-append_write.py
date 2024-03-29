#!/usr/bin/python3
"""
THis module contains a function that appends a string at
the end of text file (UTF8) and returns
the number of characters added:
"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of text file
    (UTF8) and returns the number of characters added:
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
