#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    k = len(my_list)
    if (k == 0):
        for i in my_list:
            print("{:d}".format(i))
    elif (k == 1):
        for i in my_list:
            print("{:d}".format(i))
    else:
        for i in reversed(my_list):
            print("{:d}".format(i))
