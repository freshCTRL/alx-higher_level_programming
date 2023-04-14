#!/usr/bin/python3
"""
THis module contains a function that reads
a text file (UTF8) and prints it
to stdout:
"""


def read_file(filename=""):
    """a function that reads a text file (UTF8)
    and prints it to stdout:
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
