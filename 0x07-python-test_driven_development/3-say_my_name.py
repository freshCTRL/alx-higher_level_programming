#!/usr/bin/python3
"""This module takes input of first_name and last_name
and prints the full name. if input is not string
it raises a ValueError else it prints and last name is not
provided it prints the first name
"""


def say_my_name(first_name, last_name=""):
    """a function that says a fullname based on input
    Raises: TypeError("first_name or last_name is not string")
    """
    
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
