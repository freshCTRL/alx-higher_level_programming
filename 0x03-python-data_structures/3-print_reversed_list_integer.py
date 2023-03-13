#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    k = len(mylist)//2
    for i in range(k):
        l = i + 1
        item = my_list[i]
        my_list[i] = my_list[len(my_list) - l]
        my_list[len(my_list) - l] = item
    for j in my_list:
        print("{:d}".format(j))
