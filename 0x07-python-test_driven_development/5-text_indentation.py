#!/usr/bin/python3
"""
This module prints two new line after each of
., ?, or : in a text string, if the test is not a string
an exception is raised.
"""


def text_indentation(text):
    """
    Raises: TypeError if text is not a string.
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    text = list(text)
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            j = i
            j = i+1
            while (text[j] == " "):
                text[j] = ""
                j += 1
            text.insert(j, '\n\n')
            i = j
    text = "".join(text)
    print(text, end="")
