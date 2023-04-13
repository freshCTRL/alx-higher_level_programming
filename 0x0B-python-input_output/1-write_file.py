#!/usr/bin/python3
def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8) and
    returns the number of characters written:
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
    with open(filename, mode="r+", encoding="utf-8") as f:
        t = f.read()
        return f.write(t)
