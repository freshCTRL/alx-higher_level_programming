#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = set(my_list.copy())
    my_list = list(my_list)
    sum = 0
    for i in range(len(my_list)):
        sum += my_list[i]
    return sum
