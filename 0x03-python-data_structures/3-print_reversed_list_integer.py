#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    while n > 0:
        n -= 1
        print("{:d}".format(my_list[n]))
