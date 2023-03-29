#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    j = 0

    while x > 0:
        if type(my_list[i]) == int:
            try:
                print("{:d}".format(my_list[i]), end='')
                j += 1
            except IndexError:
                raise Exception
        x -= 1
        i += 1
    print()
    return j
