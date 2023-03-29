#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    new_list = []
    for l in range(x):
        try:
            new_list.append(my_list[l])
        except IndexError:
            continue
    for i in new_list:
        print(i, end='')
    j = 0
    for s in new_list:
        j += 1
    return j
