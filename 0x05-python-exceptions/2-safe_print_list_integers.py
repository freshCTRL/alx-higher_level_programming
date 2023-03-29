#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        new_list = []
        i = 0
        for i in range(x):
            if type(my_list[i]) == int:
                new_list.append(my_list[i])
                print(my_list[i], end="")

        j = 0
        for k in new_list:
            j += 1
        print()
        return j
    except IndexError:
        print("list index out of range")
