#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if type(my_list) == list:
        if len(my_list) != 0:
            for i in reversed(my_list):
                print("{:d}".format(i))
